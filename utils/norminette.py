import subprocess
import sys
import shutil
import re
import os
from rich.console import Console
from utils.ui import print_command_execution

console = Console()

def strip_ansi(text):
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	return ansi_escape.sub('', text)

def check_norminette(file_path):
	filename = os.path.basename(file_path)

	if shutil.which("norminette") is not None:
		cmd_list = ["norminette", "-R", "CheckForbiddenSourceHeader", file_path]
		display_cmd = f"norminette -R CheckForbiddenSourceHeader {filename}"

	else:
		cmd_list = [sys.executable, "-m", "norminette", "-R", "CheckForbiddenSourceHeader", file_path]
		display_cmd = f"python -m norminette -R CheckForbiddenSourceHeader {filename}"

	print_command_execution(display_cmd)

	try:
		result = subprocess.run(cmd_list, capture_output=True, text=True)
		raw_output = result.stdout.strip()
		clean_output = strip_ansi(raw_output)

		if "Error" in clean_output:
			console.print(f"[deep_pink2]{filename}: Error![/deep_pink2]")
			lines = clean_output.split('\n')

			for line in lines:
				if "Error:" in line:
					clean_line = line.replace(file_path, filename).strip()
					console.print(f"[deep_pink2]{clean_line}[/deep_pink2]")

			print()
			return False
			
		else:
			console.print(f"[sea_green2]{filename}: OK![/sea_green2]")
			print()
			return True

	except Exception:
		console.print("[bright_black]⚠ Norminette not found (skipping)[/bright_black]")
		return True

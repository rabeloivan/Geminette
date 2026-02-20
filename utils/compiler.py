import subprocess
import os
from rich.console import Console
from utils.ui import print_command_execution

console = Console()

def compile_source(source_files, output_name, flags=None):
	if flags is None:
		flags = ["-Wall", "-Wextra", "-Werror"]

	command = ["gcc"] + flags + source_files + ["-o", output_name]
	student_file = os.path.basename(source_files[0])
	flags_str = " ".join(flags)
	display_cmd = f"gcc {flags_str} {student_file} -o {output_name}"

	print_command_execution(display_cmd)

	try:
		result = subprocess.run(
			command,
			capture_output=True,
			text=True
		)

		if result.returncode != 0:
			console.print(f"[deep_pink2]gcc: ERROR[/deep_pink2]")
			clean_err = result.stderr.replace(source_files[0], student_file)
			console.print(f"[deep_pink2]{clean_err.strip()}[/deep_pink2]")
			print()
			return False

		else:
			console.print(f"[sea_green2]gcc: OK![/sea_green2]")
			print()
			return True

	except Exception as e:
		console.print(f"[red]System Error: {e}[/red]")
		return False

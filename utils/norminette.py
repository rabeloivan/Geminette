import os
import re
import shutil
import subprocess
import sys

from rich.console import Console

from utils.ui import print_command_execution

console = Console()


def strip_ansi(text):
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)


def check_norminette(file_path):
    filename = os.path.basename(file_path)

    if shutil.which("norminette") is not None:
        cmd_list = ["norminette", "-R", "CheckForbiddenSourceHeader", file_path]
        display_cmd = f"norminette -R CheckForbiddenSourceHeader {filename}"
    else:
        cmd_list = [
            sys.executable,
            "-m",
            "norminette",
            "-R",
            "CheckForbiddenSourceHeader",
            file_path,
        ]
        display_cmd = f"python -m norminette -R CheckForbiddenSourceHeader {filename}"

    print_command_execution(display_cmd)

    try:
        result = subprocess.run(cmd_list, capture_output=True, text=True)

        if result.returncode != 0 and "No module named norminette" in result.stderr:
            raise Exception("Norminette module not found")

        raw_output = result.stdout.strip()
        clean_output = strip_ansi(raw_output)

        if "Error!" in clean_output or result.returncode != 0:
            console.print(f"[deep_pink2]{filename}: Error![/deep_pink2]")
            lines = clean_output.split("\n")

            for line in lines:
                if "Error:" in line:
                    clean_line = line.replace(file_path, filename).strip()
                    console.print(
                        f"[deep_pink2]{clean_line}[/deep_pink2]", highlight=False
                    )

            print()
            return False
        else:
            console.print(f"[sea_green2]{filename}: OK![/sea_green2]")
            print()
            return True

    except Exception:
        console.print("[yellow]Norminette not found (skipping)[/yellow]")
        print()
        return True

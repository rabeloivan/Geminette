import sys
import time
from rich.console import Console
from rich.text import Text

console = Console()

GEMINETTE_ART = """
  ▄████ ▓█████  ███▄ ▄███▓ ██▓ ███▄    █ ▓█████▄▄▄█████▓▄▄▄█████▓▓█████ 
 ██▒ ▀█▒▓█   ▀ ▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ 
▒██░▄▄▄░▒███   ▓██    ▓██░▒██▒▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   
░▓█  ██▓▒▓█  ▄ ▒██    ▒██ ░██░▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ 
░▒▓███▀▒░▒████▒▒██▒   ░██▒░██░▒██░   ▓██░░▒████▒ ▒██▒ ░   ▒██▒ ░ ░▒████▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░     ▒ ░░   ░░ ▒░ ░
  ░   ░  ░ ░  ░░  ░      ░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░   ░        ░     ░ ░  ░
░ ░   ░    ░   ░      ░    ▒ ░   ░   ░ ░    ░    ░        ░         ░   
      ░    ░  ░       ░    ░           ░    ░  ░                    ░  ░
"""

def animate_header():
	lines = GEMINETTE_ART.strip("\n").split("\n")
	num_lines = len(lines)
	loops = 3

	for i in range(loops):
		for line in lines:
			console.print(Text(line, style="deep_sky_blue1"))
			time.sleep(0.05)
		
		if i < loops - 1:
			time.sleep(0.10)

			for _ in range(num_lines):
				sys.stdout.write(f"\033[F")
				sys.stdout.write(f"\033[2K")
			
			sys.stdout.flush()
	
	print()
	msg = "Geminette version 1.0.0 (12 Feb 2026)"
	console.print(Text(f"{msg:^75s}", style="italic bright_black"))
	print()
	console.print(Text("-" * 75, style="bright_black"))
	print()

def print_command_execution(command):
	console.print(f"[bright_black]Executing: {command}[/bright_black]", highlight=False)

def print_test_pass(index, description):
	console.print(
		f"[sea_green2] ✓ [/sea_green2]"
		f"[sea_green2][{index}][/sea_green2] "
		f"[sea_green2]{description}[/sea_green2]",
		highlight=False
	)

def print_test_fail(index, description):
	console.print(
		f"[deep_pink2] ✖ [/deep_pink2]"
		f"[deep_pink2][{index}][/deep_pink2] "
		f"[deep_pink2]{description}[/deep_pink2]",
		highlight=False
	)

def print_exercise_result(exercise_name, passed, total):
	percent = (passed / total) * 100
	if percent == 100:
		console.print(f"[bold black on sea_green2] PASS [/bold black on sea_green2] {exercise_name} ({passed}/{total})\n")
	else:
		console.print(f"[bold black on deep_pink2] FAIL [/bold black on deep_pink2] {exercise_name} ({passed}/{total})\n")

def print_final_summary(results):
	console.print(Text("-" * 75, style="bright_black"))

	summary_text = []
	total_exercises = len(results)
	passed_for_score = 0
	counting_score = True

	for name, status in results:
		color = "sea_green2" if status == "OK" else "deep_pink2"
		summary_text.append(f"[{color}]{name}: {status}[/{color}]")

		if status == "OK":
			if counting_score:
				passed_for_score += 1
		else:
			counting_score = False

	print()
	console.print(f"Result:      {', '.join(summary_text)}")

	score = int((passed_for_score / total_exercises) * 100) if total_exercises > 0 else 0

	color = "sea_green2" if score >= 50 else "deep_pink2"
	console.print(f"Final score: [{color}]{score}/100[/{color}]", highlight=False)

	status_str = "PASSED" if score >= 50 else "FAILED"
	console.print(f"Status:      [{color}]{status_str}[/{color}]")

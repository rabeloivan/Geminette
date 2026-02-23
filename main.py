import importlib
import os
import re
import sys
import time

from rich.console import Console

from utils.norminette import check_norminette
from utils.ui import animate_header, print_final_summary

console = Console()


def get_current_exercise_mapping():
    current_dir = os.path.basename(os.getcwd())

    if not re.match(r"^C(0[0-9]|1[0-3])$", current_dir):
        return None, current_dir

    try:
        module = importlib.import_module(f"tests.{current_dir}")
        mapping = module.get_mapping()
        return mapping, current_dir

    except ImportError:
        error_msg = f"Error: Could not load configuration for '{current_dir}'."
        fix_msg = f"Make sure '~/Geminette/tests/{current_dir}/__init__.py' exists."
        console.print(f"[deep_pink2]{error_msg:^75s}[/deep_pink2]")
        console.print(f"[white]{fix_msg:^75s}[/white]")
        sys.exit(1)

    except AttributeError:
        error_msg = f"Error: {current_dir} module is missing 'get_mapping()' function."
        console.print(f"[deep_pink2]{error_msg:^75s}[/deep_pink2]")
        sys.exit(1)


if __name__ == "__main__":
    animate_header()

    test_map, dir_name = get_current_exercise_mapping()

    if test_map is None:
        error_msg = (
            f"Current directory '{dir_name}' does not match expected pattern (C00~13)."
        )
        fix_msg = "Please navigate to an appropriate directory to run tests."
        console.print(f"[deep_pink2]{error_msg:^75s}[/deep_pink2]")
        console.print(f"[white]{fix_msg:^75s}[/white]")
        sys.exit(1)

    display_name = f"{dir_name[0]} {dir_name[1:]}"
    targets = sys.argv[1:]
    sorted_paths = sorted(test_map.keys())

    if targets:
        filtered_paths = []

        for path in sorted_paths:
            if any(t in path for t in targets):
                filtered_paths.append(path)

        if not filtered_paths:
            error_msg = f"No exercises matched '{' '.join(targets)}'."
            console.print(f"[deep_pink2]{error_msg:^75s}[/deep_pink2]")
            sys.exit(1)

        sorted_paths = filtered_paths

    console.print(
        f"[sea_green2]{'Generating test for ' + display_name + '...':^75s}[/sea_green2]",
        highlight=False,
    )
    print()

    start_time = time.time()
    results = []
    last_was_grouped = False

    for student_file_path in sorted_paths:
        ex_name, run_func = test_map[student_file_path]

        if not os.path.exists(student_file_path):
            if not last_was_grouped:
                console.print("-" * 75, style="bright_black")
                print()

            console.print(f"[deep_pink2]Missing file: {student_file_path}[/deep_pink2]")
            results.append((ex_name, "ABSENT"))
            print()
            last_was_grouped = True
            continue

        if run_func is None:
            if not last_was_grouped:
                console.print("-" * 75, style="bright_black")
                print()

            console.print(
                f"[yellow]Test for {student_file_path} not implemented yet.[/yellow]"
            )
            results.append((ex_name, "TODO"))
            print()
            last_was_grouped = True
            continue

        last_was_grouped = False
        console.print("-" * 75, style="bright_black")
        print()

        norm_passed = check_norminette(student_file_path)
        tests_passed = run_func(student_file_path)

        if not norm_passed:
            results.append((ex_name, "NORM ERR"))
        elif not tests_passed:
            results.append((ex_name, "KO"))
        else:
            results.append((ex_name, "OK"))

    print_final_summary(results)

    elapsed = time.time() - start_time
    console.print(
        f"\n[bright_black]Test completed. Total elapsed time: {elapsed:.2f}s.[/bright_black]",
        highlight=False,
    )

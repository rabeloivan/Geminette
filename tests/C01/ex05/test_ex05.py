import os

from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import (
    print_command_execution,
    print_exercise_result,
    print_test_fail,
    print_test_pass,
)


def run_C01_ex05(student_file):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    harness_path = os.path.join(test_dir, "ex05_harness.c")
    exe_path = "./putstr"

    if not compile_source([student_file, harness_path], exe_path):
        return False

    print_command_execution(exe_path)

    test_cases = [
        "Hello World!",
        "42 is the answer.",
        "   spaces   ",
        "A",
        "",
        "\t",
        "\n",
    ]

    passed_count = 0
    total_count = len(test_cases)

    for i, expected in enumerate(test_cases, 1):
        actual, err, code = run_test_case(exe_path, input_data=expected)
        disp_exp = f'"{expected.encode("unicode_escape").decode("utf-8")}"'
        disp_act = f'"{actual.encode("unicode_escape").decode("utf-8")}"'
        desc = f"ft_putstr(str={disp_exp})"

        if actual == expected:
            print_test_pass(i, f"{desc} output {disp_act} as expected")
            passed_count += 1
        else:
            print_test_fail(i, f"{desc} output {disp_act} but expected {disp_exp}")

    print_exercise_result("ex05/ft_putstr.c", passed_count, total_count)

    if os.path.exists(exe_path):
        os.remove(exe_path)

    return passed_count == total_count

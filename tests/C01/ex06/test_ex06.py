import os

from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import (
    print_command_execution,
    print_exercise_result,
    print_test_fail,
    print_test_pass,
)


def run_C01_ex06(student_file):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    harness_path = os.path.join(test_dir, "ex06_harness.c")
    exe_path = "./strlen"

    if not compile_source([student_file, harness_path], exe_path):
        return False

    print_command_execution(exe_path)

    test_cases = [
        "Hello World!",
        "42",
        "   ",
        "",
        "A very long string to test if the while loop works properly.",
        "\n",
        "\t\t",
    ]

    passed_count = 0
    total_count = len(test_cases)

    for i, input_str in enumerate(test_cases, 1):
        actual, err, code = run_test_case(exe_path, input_data=input_str)
        expected = str(len(input_str))
        disp_str = f'"{input_str.encode("unicode_escape").decode("utf-8")}"'
        disp_exp = f"{expected.encode("unicode_escape").decode("utf-8")}"
        disp_act = f"{actual.encode("unicode_escape").decode("utf-8")}"
        desc = f"ft_strlen(str={disp_str})"

        if actual == expected:
            print_test_pass(i, f"{desc} returned {disp_act} as expected")
            passed_count += 1
        else:
            print_test_fail(i, f"{desc} returned {disp_act} but expected {disp_exp}")

    print_exercise_result("ex06/ft_strlen.c", passed_count, total_count)

    if os.path.exists(exe_path):
        os.remove(exe_path)

    return passed_count == total_count

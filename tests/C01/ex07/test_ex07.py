import os

from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import (
    print_command_execution,
    print_exercise_result,
    print_test_fail,
    print_test_pass,
)


def run_C01_ex07(student_file):
    test_dir = os.path.dirname(os.path.abspath(__file__))
    harness_path = os.path.join(test_dir, "ex07_harness.c")
    exe_path = "./rev_int_tab"

    if not compile_source([student_file, harness_path], exe_path):
        return False

    print_command_execution(exe_path)

    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        [42],
        [],
        [-3, 0, 7],
        [5, 5, 5],
        [-1, -2, -3, -4],
        [2147483647, 0, -2147483648],
    ]

    passed_count = 0
    total_count = len(test_cases)

    for i, arr in enumerate(test_cases, 1):
        size = len(arr)
        input_str = f"{size} " + " ".join(map(str, arr))
        expected = " ".join(map(str, reversed(arr))) if size > 0 else ""
        actual, err, code = run_test_case(exe_path, input_data=input_str)
        desc = f"ft_rev_int_tab(tab={arr}, size={size})"
        safe_act = f"{actual.encode("unicode_escape").decode("utf-8")}"
        safe_exp = f"{expected.encode("unicode_escape").decode("utf-8")}"
        disp_act = safe_act.replace(" ", ", ")
        disp_exp = safe_exp.replace(" ", ", ")

        if actual == expected:
            print_test_pass(i, f"{desc} set tab to [{disp_act}] as expected")
            passed_count += 1
        else:
            print_test_fail(
                i, f"{desc} set tab to [{disp_act}] but expected [{disp_exp}]"
            )

    print_exercise_result("ex07/ft_rev_int_tab.c", passed_count, total_count)

    if os.path.exists(exe_path):
        os.remove(exe_path)

    return passed_count == total_count

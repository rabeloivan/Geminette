import os
from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import print_test_pass, print_test_fail, print_exercise_result, print_command_execution

def run_C01_ex08(student_file):
	test_dir = os.path.dirname(os.path.abspath(__file__))
	harness_path = os.path.join(test_dir, "ex08_harness.c")
	exe_path = "./sort_int_tab"

	if not compile_source([student_file, harness_path], exe_path):
		return False

	print_command_execution(exe_path)

	test_cases = [
		[4, 2, 8, 5, 1],
		[1, 2, 3, 4, 5],
		[9, 7, 5, 3, 1],
		[42, 42, 42, 10, 10],
		[-5, 10, -100, 0, 3],
		[42],
		[]
	]

	passed_count = 0
	total_count = len(test_cases)

	for i, arr in enumerate(test_cases, 1):
		size = len(arr)
		input_str = f"{size} " + " ".join(map(str, arr))
		expected = " ".join(map(str, sorted(arr))) if size > 0 else ""
		actual, err, code = run_test_case(exe_path, input_data=input_str)
		desc = f"ft_sort_int_tab(tab={arr}, size={size})"
		safe_act = f"{actual.encode("unicode_escape").decode("utf-8")}"
		safe_exp = f"{expected.encode("unicode_escape").decode("utf-8")}"
		disp_act = safe_act.replace(" ", ", ")
		disp_exp = safe_exp.replace(" ", ", ")

		if actual == expected:
			print_test_pass(i, f"{desc} set tab to [{disp_act}] as expected")
			passed_count += 1
		else:
			print_test_fail(i, f"{desc} set tab to [{disp_act}] but expected [{disp_exp}]")

	print_exercise_result("ex08/ft_sort_int_tab.c", passed_count, total_count)

	if os.path.exists(exe_path):
		os.remove(exe_path)

	return (passed_count == total_count)

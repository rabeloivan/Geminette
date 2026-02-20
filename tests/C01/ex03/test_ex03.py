import os
from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import print_test_pass, print_test_fail, print_exercise_result, print_command_execution

def run_C01_ex03(student_file):
	test_dir = os.path.dirname(os.path.abspath(__file__))
	harness_path = os.path.join(test_dir, "ex03_harness.c")
	exe_path = "./div_mod"

	if not compile_source([student_file, harness_path], exe_path):
		return False
	
	print_command_execution(exe_path)

	test_cases = [
		(10, 3,				"3 1"),
		(42, 10,			"4 2"),
		(100, 25,			"4 0"),
		(0, 42,				"0 0"),
		(-10, 3,			"-3 -1"),
		(10, -3,			"-3 1"),
		(-45, -7,			"6 -3"),
		(2147483647, 10,	"214748364 7"),
		(-2147483648, 10,	"-214748364 -8"),
		(42, 2147483647,	"0 42")
	]

	passed_count = 0
	total_count = len(test_cases)

	for i, (a, b, expected) in enumerate(test_cases, 1):
		input_str = f"{a} {b}"
		actual, err, code = run_test_case(exe_path, input_data=input_str)
		desc = f"ft_div_mod(a={a}, b={b}, div, mod)"
		exp_div, exp_mod = expected.split()

		try:
			act_div, act_mod = actual.split()
		except ValueError:
			act_div = actual if actual else "CRASH"
			act_mod = "CRASH"

		disp_exp_div = exp_div.encode("unicode_escape").decode("utf-8")
		disp_exp_mod = exp_mod.encode("unicode_escape").decode("utf-8")
		disp_act_div = act_div.encode("unicode_escape").decode("utf-8")
		disp_act_mod = act_mod.encode("unicode_escape").decode("utf-8")

		if actual == expected:
			print_test_pass(i, f"{desc} set div to {disp_act_div} and mod to {disp_act_mod} as expected")
			passed_count += 1
		else:
			print_test_fail(i, f"{desc} set div to {disp_act_div} and mod to {disp_act_mod} but expected div = {disp_exp_div} and mod = {disp_exp_mod}")

	print_exercise_result("ex03/ft_div_mod.c", passed_count, total_count)

	if os.path.exists(exe_path):
		os.remove(exe_path)
	
	return (passed_count == total_count)

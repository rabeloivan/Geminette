import os
from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import print_test_pass, print_test_fail, print_exercise_result, print_command_execution

def run_C01_ex02(student_file):
	test_dir = os.path.dirname(os.path.abspath(__file__))
	harness_path = os.path.join(test_dir, "ex02_harness.c")
	exe_path = "./swap"

	if not compile_source([student_file, harness_path], exe_path):
		return False
	
	print_command_execution(exe_path)

	test_cases = [
		(42, 24),
		(-100, 50),
		(0, 42),
		(42, 42),
		(-5, -10)
	]

	passed_count = 0
	total_count = len(test_cases)

	for i, (a, b) in enumerate(test_cases, 1):
		input_str = f"{a} {b}"
		expected = f"{b} {a}"
		actual, err, code = run_test_case(exe_path, input_data=input_str)
		desc = f"ft_swap(a={a}, b={b})"
		exp_a, exp_b = expected.split()

		try:
			act_a, act_b = actual.split()
		except ValueError:
			act_a = actual if actual else "CRASH"
			act_b = "CRASH"
		
		disp_exp_a = exp_a.encode("unicode_escape").decode("utf-8")
		disp_exp_b = exp_b.encode("unicode_escape").decode("utf-8")
		disp_act_a = act_a.encode("unicode_escape").decode("utf-8")
		disp_act_b = act_b.encode("unicode_escape").decode("utf-8")

		if actual == expected:
			print_test_pass(i, f"{desc} set a to {disp_act_a} and b to {disp_act_b} as expected")
			passed_count += 1
		else:
			print_test_fail(i, f"{desc} set a to {disp_act_a} and b to {disp_act_b} but expected a = {disp_exp_a} and b = {disp_exp_b}")
		
	print_exercise_result("ex02/ft_swap.c", passed_count, total_count)

	if os.path.exists(exe_path):
		os.remove(exe_path)
	
	return (passed_count == total_count)

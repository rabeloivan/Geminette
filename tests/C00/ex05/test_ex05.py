import os
from utils.compiler import compile_source
from utils.runner import run_test_case
from utils.ui import print_test_pass, print_test_fail, print_exercise_result, print_command_execution

def generate_comb_output():
	results = []
	for i in range(0, 8):
		for j in range(i + 1, 9):
			for k in range(j + 1, 10):
				results.append(f"{i}{j}{k}")
	return ", ".join(results)

def run_C00_ex05(student_file):
	test_dir = os.path.dirname(os.path.abspath(__file__))
	harness_path = os.path.join(test_dir, "ex05_harness.c")
	exe_path = "./print_comb"

	if not compile_source([student_file, harness_path], exe_path):
		return False
	
	print_command_execution(exe_path)

	expected = generate_comb_output()
	actual, err, code = run_test_case(exe_path, input_data="")
	disp_exp = f"{expected.encode("unicode_escape").decode("utf-8")}"
	disp_act = f"{actual.encode("unicode_escape").decode("utf-8")}"
	passed = False

	if actual == expected:
		print_test_pass(1, f"ft_print_comb() output {disp_act} as expected")
		passed = True
	else:
		print_test_fail(1, f"ft_print_comb() output {disp_act} but expected {disp_exp}")
	
	print_exercise_result("ex05/ft_print_comb.c", 1 if passed else 0, 1)

	if os.path.exists(exe_path):
		os.remove(exe_path)
	
	return passed

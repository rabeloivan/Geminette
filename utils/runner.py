import subprocess

def run_test_case(executable_path, input_data=None, timeout=2):
	try:
		process = subprocess.Popen(
			[executable_path],
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			text=True
		)
		stdout_data, stderr_data = process.communicate(input=input_data, timeout=timeout)
		return stdout_data, stderr_data, process.returncode
	
	except subprocess.TimeoutExpired:
		process.kill()
		return "", "TIMEOUT", -1

	except Exception as e:
		return "", str(e), -1

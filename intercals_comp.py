from subprocess import run
import os

PROG1 = "./intervals_v1.exe"
PROG2 = "./intervals_v2.exe"
TESTCASESDIR = "interval_testcases/"
REPORTFILE = "intervals_comp_report3.txt"

test_case_files = os.listdir(TESTCASESDIR)


def report(file: str, out1: str, out2: str):
    return f"test case: {file}\n\nOutput From intervals_v1.exe\n\n{out1}\n\nOutput From intervals_v2.exe\n\n{out2}\n\n\n\n"


with open(REPORTFILE, 'w') as report_file:
    for test_case_file in test_case_files:
        rel_path = TESTCASESDIR+test_case_file
        with open(rel_path) as file:
            test_case = file.read().encode()
        res1 = run(PROG1, capture_output=True, input=test_case)
        res2 = run(PROG2, capture_output=True, input=test_case)
        out1 = res1.stdout.decode().strip()
        out2 = res2.stdout.decode().strip()

        if out1 != out2:
            line = report(test_case_file, out1, out2)
        else:
            line = f"{test_case_file} is ok"

        print(line)
        report_file.write(f"{line}\n")

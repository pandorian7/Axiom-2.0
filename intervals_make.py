
import random

TESTCASEDIR = "interval_testcases/"


def name(index: int) -> str:
    return f"intervals_testcase_{index:04}.txt"


def path(index: int) -> str:
    return TESTCASEDIR+name(index)


def generate_interval():
    start = random.randrange(1441)
    end = random.randrange(start, 1441)
    return (start, end)


def generate_testcase_str(intervals: list[tuple[int, int]]) -> str:
    string = f"{len(intervals)}\n2\n"
    for interval in intervals:
        start, end = interval
        string += f"{start} {end}\n"
    return string.strip()


def write_testcase(test_case_str: str, index: int):
    with open(path(index), 'w') as file:
        file.write(test_case_str)


def generate_testcase(index: int):
    n = random.randrange(1, 10)
    intervals = [generate_interval() for i in range(n)]
    string = generate_testcase_str(intervals)
    write_testcase(string, index)


for i in range(1000):
    generate_testcase(i)

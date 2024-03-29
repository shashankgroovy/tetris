import subprocess
from dataclasses import dataclass
from typing import Iterable

ENTRY_POINT = "./tetris"


@dataclass
class TestCase:
    name: str
    sample_input: bytes
    sample_output: Iterable[int]


def run_test(test_case: TestCase):
    p = subprocess.run(
        [ENTRY_POINT],
        input=test_case.sample_input,
        capture_output=True,
    )

    output = [int(line) for line in p.stdout.splitlines()]

    assert output == [
        test_case.sample_output
    ], f"The test with name `{test_case.name}` failed."


if __name__ == "__main__":
    test_cases = [
        TestCase("simple test", b"Q0", 2),
        TestCase("Many blocks test", ",".join(["Q0"] * 50).encode("utf-8"), 100),
    ]
    for test_case in test_cases:
        run_test(test_case)

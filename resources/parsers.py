from pathlib import Path
from typing import List


def read_data_input(file_loc: Path) -> List[str]:
    with open(file_loc) as f:
        output = [line.strip() for line in f]
    return output

def read_test_data_input(test_data: str) -> List[str]:
    return [line.strip() for line in test_data.split('\n')]
from typing import List

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

test_data = test_input.split('\n')

with open('./data/01.txt') as f:
    data = [line.strip() for line in f]

def _prep_data(input: List[str]) -> List[List[int]]:
    output: List[List[int]] = []
    current_elf: List[int] = []
    for line in input:
        if line == '':
            output.append(current_elf)
            current_elf: List[int] = []
        else:
            current_elf.append(int(line))
    return output 

def _total_calories_per_elf(input: List[List[int]]) -> List[int]:
    output = [sum(elf) for elf in input]
    return output

def get_top_calories(input: List[str], num_elves: int = 1) -> int:
    snacks_by_elf = _prep_data(input)
    total_calories_per_elf = sorted(_total_calories_per_elf(snacks_by_elf), reverse=True)
    top_elves = total_calories_per_elf[:num_elves]
    return sum(top_elves)

assert get_top_calories(test_data) == 24000
assert get_top_calories(test_data, 3) == 45000
print(get_top_calories(data)) 
print(get_top_calories(data, 3))
    
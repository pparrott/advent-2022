from typing import List, Optional, Tuple
from resources.parsers import read_data_input, read_test_data_input
from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

test_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

test_data = read_test_data_input(test_input)
data = read_data_input(Path('./data/03.txt'))

def _create_priority() -> dict[str, int]:
    priority_level = 0
    priority_dict: dict[str, int] = {}
    for letter in ascii_lowercase:
        priority_level += 1
        priority_dict[letter] = priority_level
    for letter in ascii_uppercase:
        priority_level += 1
        priority_dict[letter] = priority_level
    return priority_dict

class Rucksack():
    def __init__(self, contents: str) -> None:
        self.contents = contents
    
    def _split_rucksack(self) -> Tuple[List[str], List[str]]:
        compartment_size = int(len(self.contents)/2)
        return (list(self.contents[:compartment_size]), list(self.contents[compartment_size:]))

    def get_common_item(self) -> Optional[str]:
        compartment1, compartment2 = self._split_rucksack()
        for item in compartment1:
            if item in compartment2:
                return item
        return None

    def get_contents(self) -> str:
        return self.contents

def get_badge_from_group(elves: List[Rucksack], elves_per_group: int) -> Optional[str]:
    badge_counter: dict[str, int] = {}
    for elf in elves:
        contents_set = set(elf.get_contents())
        for item in contents_set:
            if item not in badge_counter.keys():
                badge_counter[item] = 1
            else:
                badge_counter[item] += 1
                if badge_counter[item] == elves_per_group:
                    return item
    return None

def sum_priority(data: List[str]) -> int:
    priority_sum = 0
    priority_dict = _create_priority()
    for sack in data:
        rucksack = Rucksack(sack)
        common_item = rucksack.get_common_item()
        priority_sum += priority_dict[common_item] if common_item else 0
    return priority_sum

def sum_badge_priority(data: List[str], elves_per_group: int = 3) -> int:
    priority_sum = 0
    priority_dict = _create_priority()
    counter = 0
    elf_group: List[Rucksack] = []
    for sack in data:
        elf_group.append(Rucksack(sack))
        counter += 1
        if counter == elves_per_group:
            badge = get_badge_from_group(elf_group, elves_per_group)
            priority_sum += priority_dict[badge] if badge else 0
            elf_group = []
            counter = 0
    return priority_sum



assert sum_priority(test_data) ==  157
print(sum_priority(data))
assert sum_badge_priority(test_data) == 70
print(sum_badge_priority(data))
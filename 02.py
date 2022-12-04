from pathlib import Path
from typing import List
from resources.parsers import read_data_input, read_test_data_input

test_input = """A Y
B X
C Z"""

test_data = read_test_data_input(test_input)
data = read_data_input(Path('./data/02.txt'))

SHAPE_SCORES = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

NORMALIZED_SHAPES = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

OUTCOME_POINTS = {
    'win': 6,
    'loss': 0,
    'draw': 3
}

OUTCOMES = {
    'A': {'Y': 'win', 'Z': 'loss'},
    'B': {'Z': 'win', 'X': 'loss'},
    'C': {'X': 'win', 'Y': 'loss'}
}

REVERSE_OUTCOMES = {
    'A': {'win': 'Y', 'loss': 'Z'},
    'B': {'win': 'Z', 'loss': 'X'},
    'C': {'win': 'X', 'loss': 'Y'}
}

ELF_CODE = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

def _determine_outcome(opponent_shape: str, your_shape: str) -> str:
    outcome: str
    if NORMALIZED_SHAPES[opponent_shape] == your_shape:
        outcome = 'draw'
    else:
        outcome = OUTCOMES[opponent_shape][your_shape]
    return outcome

def _point_per_match(opponent_shape: str, your_shape: str) -> int:
    result_points = OUTCOME_POINTS[_determine_outcome(opponent_shape, your_shape)]
    shape_points = SHAPE_SCORES[your_shape]
    return sum([result_points, shape_points])

def _decode_shape(your_code: str, opp_shape: str) -> str:
    match_result = ELF_CODE[your_code]
    if match_result == 'draw':
        your_shape = NORMALIZED_SHAPES[opp_shape]
    else:
        your_shape = REVERSE_OUTCOMES[opp_shape][match_result]
    return your_shape

def get_total_points(input: List[str]) -> int:
    total_points = 0
    for match in input:
        opp_shape, your_shape = match.split(' ')
        total_points += _point_per_match(opp_shape, your_shape)
    return total_points

def get_total_encrypted_points(input: List[str]) -> int:
    total_points = 0
    for match in input:
        opp_shape, your_code = match.split(' ')
        your_shape = _decode_shape(your_code, opp_shape)
        total_points += _point_per_match(opp_shape, your_shape)
    return total_points

assert get_total_points(test_data) == 15
assert get_total_encrypted_points(test_data) == 12
print(get_total_points(data))
print(get_total_encrypted_points(data))
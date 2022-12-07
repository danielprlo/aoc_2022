from enum import Enum


class GameOutcome(Enum):
    LOSE = 'lose'
    DRAW = 'draw'
    WIN = 'win'


rules = {'A': 'C', 'B': 'A', 'C': 'B'}
elf_instructions = {'X': GameOutcome.LOSE, 'Y': GameOutcome.DRAW, 'Z': GameOutcome.WIN}
outcomes = {GameOutcome.LOSE: 0, GameOutcome.DRAW: 3, GameOutcome.WIN: 6}
points = 0

for line in open('input.txt', 'r').readlines():
    plays = line.split()
    opponent_play = plays[0]
    game_outcome = elf_instructions[plays[1]]

    if game_outcome == GameOutcome.LOSE:
        my_play = rules[opponent_play]
    elif game_outcome == GameOutcome.DRAW:
        my_play = opponent_play
    else:
        my_play = list(rules.keys())[list(rules.values()).index(opponent_play)]

    points += outcomes[game_outcome]
    points += ord(my_play) - 64

print(points)

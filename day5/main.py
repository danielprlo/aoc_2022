puzzle = {}
for line in open('input.txt', 'r').readlines():
    instructions = line.strip('\n').split(' ')
    spaces_counter = 0
    crater_column = 1
    if instructions[0] != 'move':
        for instruction in instructions:
            if not instruction.isnumeric():
                if instruction == '':
                    spaces_counter += 1
                    if spaces_counter % 4 == 0:
                        crater_column += 1
                else:
                    if crater_column not in puzzle.keys():
                        puzzle[crater_column] = []

                    puzzle[crater_column].append(instruction)
                    crater_column += 1
    else:
        moving = []
        for i in range(0, int(instructions[1])):
            element = puzzle[int(instructions[3])].pop(0)
            moving.append(element)

        puzzle[int(instructions[5])] = moving + puzzle[int(instructions[5])]

result = ''
for i in range(1, len(puzzle.keys())+1):
    result += puzzle[i].pop(0).strip('[').strip(']')

print(result)

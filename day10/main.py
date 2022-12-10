data_stream = open('input.txt', 'r').readlines()


def print_crt(matrix):
    for row in matrix:
        print(row)


def get_row_crt(cycle_number):
    if cycle_number <= 40:
        return 0
    elif cycle_number <= 80:
        return 1
    elif cycle_number <= 120:
        return 2
    elif cycle_number <= 160:
        return 3
    elif cycle_number <= 200:
        return 4
    elif cycle_number <= 240:
        return 5


def get_substract(cycle_number):
    if cycle_number <= 40:
        return 0
    elif cycle_number <= 80:
        return 40
    elif cycle_number <= 120:
        return 80
    elif cycle_number <= 160:
        return 120
    elif cycle_number <= 200:
        return 160
    elif cycle_number <= 240:
        return 200


def add_pixels(crt, sprite_positions, cycle_number):
    if sprite_positions[0] == cycle_number - get_substract(cycle_number) - 1:
        crt[get_row_crt(cycle_number)][sprite_positions[0]] = '#'
    if sprite_positions[1] == cycle_number - get_substract(cycle_number) - 1:
        crt[get_row_crt(cycle_number)][sprite_positions[1]] = '#'
    if sprite_positions[2] == cycle_number - get_substract(cycle_number) - 1:
        crt[get_row_crt(cycle_number)][sprite_positions[2]] = '#'

    return crt


def main():
    x = 1
    cycle_number = 1

    crt = [['.'] * 40 for i in range(6)]
    for instruction in data_stream:
        sprite_positions = [x - 1, x, x + 1]
        instructions = instruction.strip('\n').split(' ')
        if instructions[0] == 'noop':
            add_pixels(crt, sprite_positions, cycle_number)
            cycle_number += 1
        else:
            for i in range(0, 2):
                add_pixels(crt, sprite_positions, cycle_number)
                cycle_number += 1

            x += int(instructions[1])

    print_crt(crt)


if __name__ == "__main__":
    main()

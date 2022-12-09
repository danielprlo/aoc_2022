data_stream = open('input.txt', 'r').readlines()


def main():
    h_pos = {'x': 50000, 'y': 50000}
    t_pos = {'x': 50000, 'y': 50000}
    visited = {}

    for line in data_stream:
        moves = line.strip('\n').split(' ')
        print('before move')
        print(h_pos, t_pos)
        for step in range(0, int(moves[1])):
            ## Move head
            if moves[0] == 'U':
                h_pos['y'] += 1
            elif moves[0] == 'D':
                h_pos['y'] -= 1
            elif moves[0] == 'R':
                h_pos['x'] += 1
            else:
                h_pos['x'] -= 1

            ##Move tail
            distance_x = abs(h_pos['x']) - abs(t_pos['x'])
            distance_y = abs(h_pos['y']) - abs(t_pos['y'])

            print(h_pos, t_pos)

            if abs(distance_x) > 1 or abs(distance_y) > 1:

                ## move right
                if distance_x == 2 and distance_y == 0:
                    t_pos['x'] += 1
                ## move left
                elif distance_x == -2 and distance_y == 0:
                    print('aqui')
                    t_pos['x'] -= 1
                ## move up
                elif distance_y == 2 and distance_x == 0:
                    t_pos['x'] += 1
                ## move down
                elif distance_y == -2 and distance_x == 0:
                    t_pos['y'] -= 1

                elif distance_x > 0 and distance_y > 0:
                    t_pos['x'] += 1
                    t_pos['y'] += 1
                elif distance_x < 0 and distance_y > 0:
                    t_pos['x'] -= 1
                    t_pos['y'] += 1
                elif distance_x < 0 and distance_y < 0:
                    t_pos['x'] -= 1
                    t_pos['y'] -= 1
                else:
                    t_pos['x'] += 1
                    t_pos['y'] -= 1

            visited[str(t_pos['x']) + str(t_pos['y'])] = True
        print('after')
        print(h_pos, t_pos)

    # print(matrix)
    #
    steps = 0

    for visit in visited.keys():
        steps += 1
    print('aqui')
    print(steps)


if __name__ == "__main__":
    main()

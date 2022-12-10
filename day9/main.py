data_stream = open('input.txt', 'r').readlines()


def main():
    snake = [
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000},
        {'x': 50000, 'y': 50000}
    ]
    visited = {}

    for line in data_stream:
        print(line)
        moves = line.strip('\n').split(' ')
        for step in range(0, int(moves[1])):
            ## Move head
            if moves[0] == 'U':
                snake[0]['y'] += 1
            elif moves[0] == 'D':
                snake[0]['y'] -= 1
            elif moves[0] == 'R':
                snake[0]['x'] += 1
            else:
                snake[0]['x'] -= 1

            for i in range(0,10):
                ##Move tail
                distance_x = abs(snake[i]['x']) - abs(snake[i+1]['x'])
                distance_y = abs(snake[i]['y']) - abs(snake[i+1]['y'])

                if abs(distance_x) > 1 or abs(distance_y) > 1:
                    ## move right
                    if distance_x == 2 and distance_y == 0:
                        snake[i+1]['x'] += 1
                    ## move left
                    elif distance_x == -2 and distance_y == 0:
                        snake[i+1]['x'] -= 1
                    ## move up
                    elif distance_y == 2 and distance_x == 0:
                        snake[i+1]['y'] += 1
                    ## move down
                    elif distance_y == -2 and distance_x == 0:
                        snake[i+1]['y'] -= 1
                    elif distance_x > 0 and distance_y > 0:
                        snake[i+1]['x'] += 1
                        snake[i+1]['y'] += 1
                    elif distance_x < 0 and distance_y > 0:
                        snake[i+1]['x'] -= 1
                        snake[i+1]['y'] += 1
                    elif distance_x < 0 and distance_y < 0:
                        snake[i+1]['x'] -= 1
                        snake[i+1]['y'] -= 1
                    else:
                        snake[i+1]['x'] += 1
                        snake[i+1]['y'] -= 1
                if i == 9:
                    visited[str(snake[i+1]['x']) + str(snake[i+1]['y'])] = True

    print(snake)
    print(len(visited.keys())+1)


if __name__ == "__main__":
    main()

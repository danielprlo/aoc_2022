data_stream = open('input.txt', 'r').readlines()


def main():
    visible = 0
    matrix = [line.strip() for line in data_stream]

    for i, forest in enumerate(matrix):
        for j, tree in enumerate(forest):
            ## Surroundings
            if i == 0 or i == len(forest) - 1 or j == len(forest) - 1 or j == 0:
                visible += 1
            else:
                ## left
                visible_left = True
                for x in range(i-1, -1, -1):
                    if matrix[i][j] <= matrix[x][j]:
                        visible_left = False
                        break
                ## right
                visible_right = True
                for x in range(i+1, len(forest)):
                    if matrix[i][j] <= matrix[x][j]:
                        visible_right = False
                        break
                ## top DONE
                visible_top = True
                for x in range(j-1, -1, -1):
                    if matrix[i][j] <= matrix[i][x]:
                        visible_top = False
                        break

                ## bottom DONE
                visible_bottom = True
                for x in range(j+1, len(forest)):
                    if matrix[i][j] <= matrix[i][x]:
                        visible_bottom = False
                        break

                if visible_left or visible_right or visible_top or visible_bottom:
                    visible += 1

    print(visible)


if __name__ == "__main__":
    main()

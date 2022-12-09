data_stream = open('input.txt', 'r').readlines()


def main():
    visible = 0
    matrix = [line.strip() for line in data_stream]
    max_tree = 0

    for i, forest in enumerate(matrix):
        for j, tree in enumerate(forest):
            show = False
            if matrix[i][j] == '6':
                show = True

            if show: print(matrix[i][j])
            ## top
            max_tree_top = 0
            for x in range(i-1, -1, -1):
                if matrix[i][j] <= matrix[x][j]:
                    max_tree_top += 1
                    break
                max_tree_top += 1
            ## bottom
            max_tree_bottom = 0
            for x in range(i+1, len(forest)):
                if matrix[i][j] <= matrix[x][j]:
                    max_tree_bottom += 1
                    break
                max_tree_bottom += 1
            ## left
            max_tree_left = 0
            for x in range(j-1, -1, -1):
                if show: print('here', i, j, x)
                if matrix[i][j] <= matrix[i][x]:
                    max_tree_left += 1
                    break
                max_tree_left += 1

            ## right
            max_tree_right = 0
            for x in range(j+1, len(forest)):
                if matrix[i][j] <= matrix[i][x]:
                    max_tree_right += 1
                    break
                max_tree_right += 1

            total_count_tree = max_tree_left * max_tree_right * max_tree_top * max_tree_bottom
            if show:
                print(max_tree_left, max_tree_right, max_tree_top, max_tree_bottom)
            if total_count_tree > max_tree:
                max_tree = total_count_tree

    print(max_tree)


if __name__ == "__main__":
    main()

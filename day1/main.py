top_1 = top_2 = top_3 = 0
calories_count = 0
for line in open('input.txt', 'r').readlines():
    if line == '\n':
        if calories_count > top_1:
            top_3 = top_2
            top_2 = top_1
            top_1 = calories_count
        elif calories_count > top_2:
            top_3 = top_2
            top_2 = calories_count
        elif calories_count > top_3:
            top_3 = calories_count
        calories_count = 0
    else:
        calories_count += int(line)

print(top_1 + top_2 + top_3)

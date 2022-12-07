duplicated = 0
for section_assignment in open('input.txt', 'r').readlines():
    assignments = section_assignment.strip('\n').split(',')
    sections_first_elf = assignments[0].split('-')
    sections_second_elf = assignments[1].split('-')

    numbers_array = []
    found = False

    for i in range(int(sections_first_elf[0]), int(sections_first_elf[1])+1):
        numbers_array.append(i)

    for i in range(int(sections_second_elf[0]), int(sections_second_elf[1])+1):
        if i in numbers_array:
            found = True
            break

    if found:
        duplicated += 1

print(duplicated)

elfs_groups_items = []
common_items = []

for rucksack in open('input.txt', 'r').readlines():
    elfs_groups_items.append(rucksack.replace('\n', ''))
    itemsFound = []
    if len(elfs_groups_items) == 3:
        badge = ''
        for item in elfs_groups_items[0]:
            if item in elfs_groups_items[1]:
                itemsFound.append(item)
        for item in elfs_groups_items[2]:
            if item in itemsFound:
                badge = item

        common_items.append(badge)
        elfs_groups_items = []

total = 0

for char in common_items:
    total += ord(char) - 38 if char.isupper() else ord(char) - 96

print(total)

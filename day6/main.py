data_stream = open('input.txt', 'r').read().strip('\n')
characters = []
position = -1

for index, char in enumerate(data_stream):
    if char not in characters:
        characters.append(char)
        if len(characters) == 14:
            print(index + 1)
            break
    else:
        characters = characters[characters.index(char)+1::]
        characters.append(char)



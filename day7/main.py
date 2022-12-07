data_stream = open('input.txt', 'r').readlines()


def instruction_type(instruction):
    if '$' in instruction:
        if 'cd ..' in instruction:
            return 'up'
        elif 'cd' in instruction:
            return 'down'
        else:
            return 'ls'
    elif 'dir' in instruction:
        return 'dir'
    else:
        return 'file'


def find_folder_to_delete(directory):
    total_space = 70000000
    unused_space_needed = 30000000

    total_space_used = directory['/']['total']
    available_space = total_space - total_space_used

    to_free = unused_space_needed - available_space

    candidates_folders_to_delete = []
    for folder in directory:
        if 'total' in directory[folder]:
            if directory[folder]['total'] > to_free:
                candidates_folders_to_delete.append(directory[folder]['total'])

    candidates_folders_to_delete.sort()
    print(candidates_folders_to_delete[0])


def main():
    directory = {'/': {}}

    path = '/'
    for line in data_stream:
        instruction = instruction_type(line)
        stripped_line = line.strip('\n')
        if instruction == 'dir':
            directory[path + stripped_line.replace('dir ', '') + '/'] = {}
        if instruction == 'down':
            path = path + stripped_line.replace('$ cd ', '') + '/'
            directory[path] = {}
        if instruction == 'up':
            path = path[0:path.rindex('/') - 1]

        if instruction == 'file':
            info_file = line.split(' ')

            directory[path][len(directory[path])] = info_file[0]
            if 'total' in directory[path]:
                directory[path]['total'] += int(info_file[0])
            else:
                directory[path]['total'] = int(info_file[0])

            parents_path = path
            while parents_path.rfind('/') > 0:
                parents_path = parents_path.rstrip('/')
                parents_path = parents_path[0:parents_path.rfind('/') + 1]
                if 'total' in directory[parents_path]:
                    directory[parents_path]['total'] += int(info_file[0])
                else:
                    directory[parents_path]['total'] = int(info_file[0])

    find_folder_to_delete(directory)


if __name__ == "__main__":
    main()

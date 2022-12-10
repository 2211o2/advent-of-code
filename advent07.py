from collections import defaultdict #

def main():
    with open('inputs/input07', 'r', encoding="utf-8") as f:
        lines = f.readlines()
        
    directories = defaultdict(int)
    curr_dir = []

    for l in lines:
        if l.startswith("$ cd"):
            dir_name = l.split()[2]
            
            if dir_name == "..":
                curr_dir.pop()
            elif dir_name == "/":
                curr_dir = ["root"]
            else:
                curr_dir.append(dir_name)

            print(curr_dir)

        elif l.startswith("$ ls"):
            filename = '/'.join(curr_dir)

            if filename not in directories:
                directories[filename] = 0

        else:
            if l.split()[0].isnumeric():
                directories['/'.join(curr_dir)] += int(l.split()[0])

    print(directories)
    print(sum([x for x in directories.values() if x <= 100_000]))

def part_two(directories):
    available = 70000000
    need      = 30000000

if __name__ == '__main__':
    main()
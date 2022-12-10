def main():
    with open('inputs/input07', 'r', encoding="utf-8") as f:
        lines = f.readlines()
    
    directories = parse_input(lines)
    part_one(directories)
    part_two(directories)

def parse_input(lines):
    directories = {}
    curr_dir = []

    for l in lines:
        if l.startswith("$ cd"):
            dir_name = l.split()[2]
            
            if dir_name == "..":
                curr_dir.pop()
            elif dir_name == "/":
                curr_dir = [""]
            else:
                curr_dir.append(dir_name)

        elif l.startswith("$ ls"):
            filename = '/'.join(curr_dir)

            if filename not in directories:
                directories[filename] = 0

        else:
            size = l.split()[0]
            if size.isnumeric():
                for i in range(1, len(curr_dir) + 1):
                    directories[ '/'.join(curr_dir[:i]) ] += int(size)
    
    return directories

def part_one(directories):
    print(sum([x for x in directories.values() if x <= 100_000]))

def part_two(directories):
    available   = 70_000_000
    needed      = 30_000_000

if __name__ == '__main__':
    main()
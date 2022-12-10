def main():
    with open('inputs/input03') as file:
        lines = file.readlines()

    part_one(lines)
    part_two(lines)

def get_priority(char):
    priority = 0
    if char.islower():
        priority = ord(char) - ord('a') + 1
    elif char.isupper():
        priority = ord(char) - ord('A') + 27
    return priority

# part one
def part_one(lines):
    sum = 0
    for l in lines:
        first, second = l[:len(l)//2], l[len(l)//2:]
        sum += find_shared(first, second)
    print(sum)

def find_shared(first, second):
    shared = []
    priorities = 0

    for x in first:
        for y in second:
            if (y is x) and (y not in shared):
                shared.append(y)
                priorities += get_priority(x)
    
    return priorities

# part two
def part_two(lines):
    sum = 0

    for l in range(0, len(lines), 3):
        sum += find_badge(lines[l].split("\n")[0], lines[l+1].split("\n")[0], lines[l+2].split("\n")[0])
    
    print(sum)

def find_badge(first, second, third):
    priorities = 0
    shared = set(first).intersection( set(second), set(third) )

    for s in shared:
        priorities = get_priority(s)

    return priorities

if __name__ == '__main__':
    main()
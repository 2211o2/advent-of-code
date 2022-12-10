def main():
    with open('inputs/input05', 'r', encoding="UTF-8") as file:
        lines = file.readlines()

    # does the heavy lifting ;)
    layout, instructions = parse_input(lines)
    stacks = build_stacks(layout)

    # part_one(instructions, stacks)
    part_two(instructions, stacks)

    print_stacks(stacks)


def print_stacks(stacks):
    # prints the crate at the top of each stack
    for i in range(1, len(stacks) + 1):
        print(stacks[i].pop( -len(stacks[i]) ), end='')
    print("")


# CRATE MOVER 9000
def part_one(instructions, stacks):
    for i in instructions:
        move, source, dest = int(i[0]), int(i[1]), int(i[2])

        movement = []
        for _ in range(0, move):
            movement.append(stacks[source].pop( -len(stacks[source]) ))
            stacks[dest].insert(0, movement.pop(0))

# CRATE MOVER 9001
def part_two(instructions, stacks):
    # sooo scuffed lol
    for i in instructions:
        move, source, dest = int(i[0]), int(i[1]), int(i[2])

        movement = [x for x in stacks[source][:move] if x]

        for _ in range(0, move):
            stacks[source].pop( -len(stacks[source]) )

        movement.extend(stacks[dest])
        stacks[dest] = movement.copy()

def parse_input(lines):
    layout = []
    instructions = []

    for l in lines:
        if l == "\n":
            break

        layout.append(l)

    for l in lines:           
        if (l in layout) or (l == "\n"):
            continue    
        
        str = l.split("\n")[0].split()
        str = [x for x in str if x.isdigit()]

        instructions.append(str)
    
    return layout, instructions

def build_stacks(layout):
    stacks = { int(i): [] for i in layout.pop().split() }

    rows = []
    for l in layout:
        rows.append([l[i * 4 + 1] for i in range( len(l) // 4 )])
    
    for x in range(0, len(stacks)):
        for y in range(0, len(rows)):
            if rows[y][x].isspace():
                continue
            stacks.get(x+1).append(rows[y][x])
    
    return stacks
    
if __name__ == '__main__':
    main()
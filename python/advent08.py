import sys

def main():
    with open(sys.path[0] + '/../inputs/input08', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    trees = [ [ int(tree) for tree in l.split("\n")[0] ] for l in lines ]

    part_one(trees)
    part_two(trees)

def part_one(trees):
    # get tree
    # get the trees around that tree
    # mark visibility

    print(trees)

def part_two(trees):
    print("hi")

if __name__ == '__main__':
    main()
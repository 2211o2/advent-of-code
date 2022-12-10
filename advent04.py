def main():
    with open('inputs/input04') as file:
        lines = file.readlines()

    assignment = []

    for l in lines:
        assignment.append(l.split("\n")[0].split(","))

    subsets = 0
    overlaps = 0
    # [[ 0-1 ],[ 2-3 ]] in [[[ 0-1 ],[ 2-3 ]] \\ [[ 4-5 ],[ 6-7 ]]]
    for pairs in assignment:
        ranges = []
        
        # [ 0-1 ] in [[ 0-1 ],[ 2-3 ]]
        for elf in pairs:
            low = int(elf.split("-")[0])
            high = int(elf.split("-")[1])
            curr_range = list( range(low, high+1) )
            ranges.append(curr_range)

        # part one
        # ugliest shit in the world but it work :)
        if set(ranges[0]).issubset(set(ranges[1])) or set(ranges[1]).issubset(set(ranges[0])):
            subsets += 1

        # part two
        if set(ranges[0]).intersection(set(ranges[1])):
            overlaps += 1

    print("part 1:", subsets, "\t\tpart 2:", overlaps)

if __name__ == '__main__':
    main()
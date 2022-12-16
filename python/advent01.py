import sys

max_elves = 3

def main():
    with open(sys.path[0] + '/../inputs/input01', 'r', encoding="utf-8") as f:
        lines = f.readlines()

    elves = []
    sum = 0
    last_line = lines[-1]

    for l in lines:
        if (not l.strip()) or (l is last_line):
            elves.append(sum)
            sum = 0
        else:
            sum += int(l)

    elves.sort(reverse=True)

    cal_count = 0
    for i in range(0, max_elves):
        cal_count += elves[i]
    
    print(cal_count)

if __name__ == '__main__':
    main()
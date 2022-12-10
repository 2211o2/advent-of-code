def main():
    with open('inputs/input06', 'r', encoding="utf-8") as f:
    # with open('inputs/test06', 'r', encoding="utf-8") as f:
        line = f.readline()
        
    part_one(line)
    part_two(line)

def part_one(str):
    packet = []

    packet.append(str[0])
    for c in range(1, len(str)):
        packet.append(str[c])

        if len(packet) > 4:
            packet.pop(0)

        if len(set(packet)) == 4:
            print(c+1)
            break

def part_two(str):
    message = []

    message.append(str[0])
    for c in range(1, len(str)):
        message.append(str[c])

        if len(message) > 14:
            message.pop(0)

        if len(set(message)) == 14:
            print(c+1)
            break

if __name__ == '__main__':
    main()
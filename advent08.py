def main():
    with open('inputs/test08', 'r', encoding="utf-8") as f:
        lines = f.readlines()
    
    trees = [ [ int(t) for t in line.strip() ] for line in lines]
    visible = (len(trees) * 2) + ((len(trees[0]) - 2) * 2)

    # removing edge rows
    trees.remove(trees[0])
    trees.remove(trees[len(trees)-1])
    # removing edge cols
    for i in range(len(trees)):
        trees[i].remove(trees[i][0])
        trees[i].remove(trees[i][len(trees[0])-1])

    for i in range(0, len(trees)-1):
        row = trees[i]
        
        for j in range(0, len(trees[0])-1):
            col = list(zip(*trees))[j]

            current_tree = trees[i][j]

            # if all(row[0:i] < current_tree) or all(row[i+1:] < current_tree) or all(col[0:j] < current_tree) or all(col[j+1:] < current_tree):
            #     total += 1

    print(visible) 

def check_visibility(current_tree, line, i):
    return all(line[0:i] < current_tree) or all(line[i+1:] < current_tree)

if __name__ == '__main__':
    main()
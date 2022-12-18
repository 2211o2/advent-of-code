def main(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.readlines()
    
    trees = [ [ int(t) for t in line.strip() ] for line in lines]
    visible = (len(trees) * 2) + ((len(trees[0]) - 2) * 2)

    # removing edge rows
    trees.remove(trees[0])
    trees.remove(trees[len(trees)-1])
    # removing edge cols
    for i in range(len(trees)):
        trees[i].remove(trees[i][0])
        trees[i].remove(trees[i][len(trees[i])-1])

    for i in range(0, len(trees)):
        row = trees[i]        
        for j in range(0, len(trees[0])):
            col = list(zip(*trees))[j]
            current_tree = trees[i][j]

            if max(above_trees) < current_tree or max(below_trees) < current_tree or max(left_trees) < current_tree or max(right_trees) < current_tree:
                visible += 1

    print(visible)
    return visible

if __name__ == '__main__':
    main('inputs/test08')
    # main('inputs/input08')

assert(main('inputs/test08') == 21)
# assert(main('inputs/input08') == 1816)
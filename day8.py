with open('./inputs/day8.txt') as f:
    inputLines = f.readlines()

    tree_grid = []
    visible_trees = 0
    row_a = 1

    for line in inputLines:
        col = 1
        line = line.replace('\n', '')

        for char in line:
            tree_grid.append([row_a, col, char, False])
            col = col + 1
        row_a = row_a + 1

    row_b = 1
    col = 1
    while row_b < row_a:
        max_row_height = 0
        max_col_height = 0
        for tree in tree_grid:
            if tree[0] == row_b:
                if int(tree[2]) > max_row_height:
                    max_row_height = int(tree[2])
                    tree[3] = True
            if tree[1] == col:
                if int(tree[2]) > max_col_height:
                    max_col_height = int(tree[2])
                    tree[3] = True
        row_b = row_b + 1
        col = col + 1

    tree_grid = tree_grid[::-1]

    row_b = 1
    col = 1

    while row_b < row_a:
        max_row_height = 0
        max_col_height = 0
        for tree in tree_grid:
            if tree[0] == row_b:
                if int(tree[2]) > max_row_height:
                    max_row_height = int(tree[2])
                    tree[3] = True
            if tree[1] == col:
                if int(tree[2]) > max_col_height:
                    max_col_height = int(tree[2])
                    tree[3] = True
        row_b = row_b + 1
        col = col + 1

    for tree in tree_grid:
        if tree[3]:
            visible_trees += 1

    print(visible_trees)

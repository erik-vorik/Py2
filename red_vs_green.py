import re


# input the grid size and check the grid for validity
def is_grid_valid(s):
    pattern = r"((\d+)\s*,\s*(\d+)\s*$)"
    match = re.search(pattern, s)
    if match is None:
        print('wrong format')
        return False
    # print(match.groups())

    try:
        a = int(match.group(2))
        b = int(match.group(3))
    except ValueError:
        print("Value Error either in X or Y")
        return False
    if a <= b < 1000:
        print('check passed successfully')
        return True
    print('False')
    return False


def input_grid_size():
    grid_size =input('Type size of grid in the format x,y:')

    # print(grid_size)
    while not is_grid_valid(grid_size):
        print('in the while loop')
        grid_size = input('Type x,y (size of grid):')
        if is_grid_valid(grid_size):
            break

    r_c_lst = grid_size.split(sep=',')
    c = int(r_c_lst[0])
    r = int(r_c_lst[1])
    # print(f'cols={c} rows={r}')
    return r, c


# initial values of the cells in the grid
def is_row_valid(row_str, n):
    pattern = r"\b([0-1]{%d})\b" % n
    match = re.search(pattern, row_str)
    if match is None:
        # print(match)
        return False
    # print(match.group(0))
    return True


def is_coord_num_valid(coord_num_str, x_grid, y_grid):
    pattern = r"((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*$)"
    match = re.search(pattern, coord_num_str)
    if match is None:
        return False
    x_cell = int(match.group(2))
    y_cell = int(match.group(3))
    if 0 <= x_cell <= x_grid - 1 and \
            0 <= y_cell <= y_grid - 1:
        # print(match)
        return True
    return False


def input_grid(size):
    """creates the initial grid and setts the values of each cell from the user's input"""
    grid_fill = list()
    cols, rows = size[1], size[0]
    for i in range(rows):
        string_input_row = input(f'row {i} --> ')
        while not is_row_valid(string_input_row, cols):
            string_input_row = input(f'row {i} --> ')
        grid_fill.append([int(x) for x in string_input_row])
    return grid_fill


def input_coord_cell_gen(size):
    """takes the user input for coordinates of a cell and number of generation"""
    coord_num = input('Coordinates of a cell and a number of generation -->')
    cols, rows = size[1], size[0]
    while not is_coord_num_valid(coord_num, cols, rows):
        coord_num = input('Enter in format x1,y1,num_of_gen -->')
    # print(coord_num, type(coord_num))
    x_c, y_c, n_gen = [int(x) for x in coord_num.split(',')]
    return x_c, y_c, n_gen


# visualize the grid with values
def grid_vizualize(matrix):
    """vizualizes the initial grid /for testing purposes/"""
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            print(matrix[i][k], end='')
        print()
    # print(matrix)


def next_gen(old_matrix):
    nextmatrix = list()  # is it possible rigid size --- DONE it using list of list of Nones
    rows = len(old_matrix)
    for i in range(rows):
        temp_cols = list()
        cols = len(old_matrix[i])
        for k in range(cols):
            temp_cols.append(None)
        nextmatrix.append(temp_cols)

    for row in range(rows):
        cols = len(old_matrix[row])
        for col in range(cols):
            cell_val = old_matrix[row][col]
            greens_count = count_green_neighbors(row, col, old_matrix, size)
            if cell_val == 1 and greens_count in [0, 1, 4, 5, 7, 8]:  # change in next generation     1 -- > 0
                nextmatrix[row][col] = 0
            elif cell_val == 0 and greens_count in [3, 6]:  # change in next generation     0 -- > 1
                nextmatrix[row][col] = 1
            else:
                nextmatrix[row][col] = cell_val  # stay unchanged in next generation 0 -- > 0 & 1 -- > 1

    return nextmatrix


def count_green_neighbors(row_center_cell, col_center_cell, curr_mat, size):
    # point the cell in question about its neighbors
    cell_center = curr_mat[row_center_cell][col_center_cell]

    greens_count = 0
    # the loop roams one cell away to check neighboring cells
    # and traverses this domain row by row left to right
    for i in range(3):  # for row in [row_center_cell-1, row_center_cell, row_center_cell+1]
        roam_cell_row = row_center_cell + i - 1
        if roam_cell_row < 0 or roam_cell_row > size[1] - 1:
            continue
        for k in range(3):
            roam_cell_col = col_center_cell + k - 1
            if roam_cell_col < 0 or roam_cell_col > size[0] - 1:
                continue
            if roam_cell_col == col_center_cell and roam_cell_row == row_center_cell:
                continue

            roam_cell = curr_mat[roam_cell_row][roam_cell_col]

            if roam_cell == 1:
                greens_count += 1
    return greens_count


def is_cell_green(matrix, r, c):
    return matrix[r][c] == 1
    # if matrix[r][c] == 1:
    #     return True
    # return False


def counts_cell_in_green(matrix, gen_nums, r, c, size):
    times_cell_is_green = 0
    old_matrix = matrix
    if is_cell_green(old_matrix, r, c):
        times_cell_is_green += 1
    print(f'Generation 0\ncell @ row:{r} col:{c} -- > times green:{times_cell_is_green}')
    for gen in range(1, gen_nums + 1):
        new_matrix = next_gen(old_matrix)
        if is_cell_green(new_matrix, r, c):
            times_cell_is_green += 1
        print(f'Generation {gen}\ncell @ row:{r} col:{c} -- > times green:{times_cell_is_green}')
        grid_vizualize(new_matrix)
        old_matrix = new_matrix
    return times_cell_is_green


size = input_grid_size()
start_grid = input_grid(size)
c = input_coord_cell_gen(size)
cell_to_check = (c[1], c[0])  # row , col
final_gen_num = c[2]

print('START the GAME')
occur_cell_in_green = counts_cell_in_green(start_grid, final_gen_num, cell_to_check[0], cell_to_check[1], size)
print(f'Result: {occur_cell_in_green}')

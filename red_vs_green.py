import re


# input the grid size and check the grid for validity
def is_grid_valid(s):
    pattern = r"((\d+)\s*,\s*(\d+)\s*$)"
    match = re.search(pattern, s)
    if match is None:
        print('wrong format')
        return False
    print(match.groups())

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
    grid_size = input('Type size of grid in the format x,y:')

    print(grid_size)
    while not is_grid_valid(grid_size):
        print('in the while loop')
        grid_size = input('Type x,y (size of grid):')
        if is_grid_valid(grid_size):
            break

    size_lst = grid_size.split(sep=',')
    cols = int(size_lst[0])
    rows = int(size_lst[1])
    print(f'x={cols} y={rows}')
    return rows, cols

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
        print(match)
        return True
    return False


def initiate_grid():
    grid_fill = list()
    for i in range(rows):
        string_input_row = input(f'row {i} --> ')
        while not is_row_valid(string_input_row, cols):
            string_input_row = input(f'row {i} --> ')
        grid_fill.append([int(x) for x in string_input_row])
    return grid_fill


def coord_cell_gen():
    coord_num = input('Coordinates of a cell and a number of generation -->')
    while not is_coord_num_valid(coord_num, cols, rows):
        coord_num = input('Enter in format x1,y1,num_of_gen -->')
    print(coord_num, type(coord_num))
    x_c, y_c, n_gen = [int(x) for x in coord_num.split(',')]
    return x_c, y_c, n_gen


# visualize the grid with values
def grid_vizualize():
    for i in range(len(grid)):
        for k in range(len(grid[i])):
            print(grid[i][k], end='')
        print()
    print(grid)


def next_gen(TODO):
    result = list()  # is it possible rigid size

    def count_green_neighbors(r, c):
        pass


size = input_grid_size()
cols, rows = size[1], size[0]
grid = initiate_grid()
c = coord_cell_gen()
cell_to_check = (c[0], c[1])
num_gen = c[2]
grid_vizualize()

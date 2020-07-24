import re


# input the grid size and check the grid dimensions for validity
def is_grid_valid(s):
    pattern = r"((\d+)\s*,\s*(\d+)\s*$)"
    match = re.search(pattern, s)
    if match is None:
        print('wrong format')
        return False

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
    while not is_grid_valid(grid_size):
        print('in the while loop')
        grid_size = input('Type x,y (size of grid):')
        if is_grid_valid(grid_size):
            break

    r_c_lst = grid_size.split(sep=',')
    c = int(r_c_lst[0])
    r = int(r_c_lst[1])
    return r, c

# input initial values of the cells in the grid
def is_row_valid(row_str, n):
    pattern = r"\b([0-1]{%d})\b" % n
    match = re.search(pattern, row_str)
    if match is None:
        return False
    return True
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

# input of coordinates of the cell in question and total number of generations to be made
def is_coord_num_valid(coord_num_str, x_grid, y_grid):
    pattern = r"((\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*$)"
    match = re.search(pattern, coord_num_str)
    if match is None:
        return False
    x_cell = int(match.group(2))
    y_cell = int(match.group(3))
    if 0 <= x_cell <= x_grid - 1 and \
            0 <= y_cell <= y_grid - 1:
        return True
    return False
def input_coord_cell_gen(size):
    """takes the user input for coordinates of a cell and number of generation"""
    coord_num = input('Coordinates of a cell and a number of generation x,y,gen -->')
    cols, rows = size[1], size[0]
    while not is_coord_num_valid(coord_num, cols, rows):
        coord_num = input('Enter in format x1,y1,num_of_gen -->')
    x_c, y_c, n_gen = [int(x) for x in coord_num.split(',')]
    return x_c, y_c, n_gen
def counts_cell_is_green(gen_obj, input_coordCell_genNum):
    gen_num= input_coordCell_genNum[2]
    r=input_coordCell_genNum[1]
    c=input_coordCell_genNum[0]

    times_cell_is_green = 0
    if gen_obj.grid[r][c].is_cell_green():
        times_cell_is_green += 1
    print(f'Generation 0\ncell @ row:{r} col:{c} -- > times green:{times_cell_is_green}')
    for gen in range(1, gen_num + 1):
        gen_obj.create_next_generation()
        if gen_obj.grid[r][c].is_cell_green():
            times_cell_is_green += 1
        print(f'Generation {gen}\ncell @ row:{r} col:{c} -- > times green:{times_cell_is_green}')
        gen_obj.grid_vizualize()
    return times_cell_is_green


class Generation:

    def __init__(self, matrix):
        matrix_red_green = list()
        for i in range(len(matrix)):
            temp_row=list()
            for k in range(len(matrix[0])):
                if matrix[i][k] == 1:
                    temp_row.append(Green(i, k, 0))
                elif matrix[i][k] == 0:
                    temp_row.append(Red(i, k, 0))
            matrix_red_green.append(temp_row)
        self.grid = matrix_red_green

    def count_green_neighbors(self, row_center_cell, col_center_cell):
        # point the cell in question about its neighbors
        cell_center = self.grid[row_center_cell][col_center_cell]
        rows = len(self.grid)
        cols = len(self.grid[0])
        greens_count = 0
        # the loop roams one cell away to check neighboring cells
        # and traverses this domain row by row left to right
        for i in range(3):  # for row in [row_center_cell-1, row_center_cell, row_center_cell+1]
            roam_cell_row = row_center_cell + i - 1
            if roam_cell_row < 0 or roam_cell_row > rows - 1:
                continue
            for k in range(3):
                roam_cell_col = col_center_cell + k - 1
                if roam_cell_col < 0 or roam_cell_col > cols - 1:
                    continue
                if roam_cell_col == col_center_cell and roam_cell_row == row_center_cell:
                    continue

                roam_cell = self.grid[roam_cell_row][roam_cell_col]

                if roam_cell.is_cell_green():
                    greens_count += 1
        return greens_count
    def create_next_generation(self):
        nextmatrix = list()  # is it possible rigid size --- DONE it using list of list of Nones
        rows = len(self.grid)
        for i in range(rows):
            temp_cols = list()
            cols = len(self.grid[i])
            for k in range(cols):
                temp_cols.append(None)
            nextmatrix.append(temp_cols)

        for row in range(rows):
            cols = len(self.grid[row])
            for col in range(cols):
                greens_count = self.count_green_neighbors(row_center_cell=row, col_center_cell=col)
                cell = self.grid[row][col]
                #if cell_val == 1 and greens_count in [0, 1, 4, 5, 7, 8]:  # change in next generation     1 -- > 0
                #    nextmatrix[row][col] = 0
                #elif cell_val == 0 and greens_count in [3, 6]:  # change in next generation     0 -- > 1
                #    nextmatrix[row][col] = 1
                #else:
                #    nextmatrix[row][col] = cell_val  # stay unchanged in next generation 0 -- > 0 & 1 -- > 1
                nextmatrix[row][col] = cell.state_in_next_gen(greens_count)
        self.grid = nextmatrix
    def grid_vizualize(self):
        """vizualizes grid with its values /for testing purposes/"""
        for i in range(len(self.grid)):
            for k in range(len(self.grid[i])):
                print(f'{self.grid[i][k].color:>7}', end=' ')
            print()
class Cell:
        def __init__(self,r,c,cur_gen):
            self.row = r
            self.col = c
            self.gen = cur_gen

        def is_cell_green(self):
            return isinstance(self, Green)
class Green(Cell):
    value = 1
    color = 'green'

    def state_in_next_gen(self,green_neig_count):
        if green_neig_count in [0, 1, 4, 5, 7, 8]:              # change in next generation     1 -- > 0
            return Red(self.row, self.col, self.gen+1 )
        return Green(self.row, self.col, self.gen+1)  # stay same in next generation  1 -- > 1
class Red(Cell):
    value = 0
    color = 'red'

    def state_in_next_gen(self,green_neig_count):
        if green_neig_count in [3, 6]:                          # change in next generation     0 -- > 1
            return Green(self.row, self.col, self.gen+1)
        return Red(self.row, self.col, self.gen+1)    # stay same in next generation  0 -- > 0


size = input_grid_size()
gen_zero = Generation(input_grid(size))
gen_zero.grid_vizualize()
coorCell_genNum = input_coord_cell_gen(size)


print('START the GAME')
times_green = counts_cell_is_green(gen_zero, coorCell_genNum)
print(f'Result: {times_green}')

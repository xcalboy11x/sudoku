def print_board(grid):
    for row in range(9):
        line = ""
        for col in range(9):
            if col % 3 == 0:
                line += "|" + str(grid[row][col]) + " "
            else:
                if col == 8:
                    line += str(grid[row][col]) + "|"
                else:
                    line += str(grid[row][col]) + " "
        if row % 3 == 0:
            print("---------------------")
        print(line)
        if row % 8 == 0 and row != 0:
            print("---------------------")

def check_board(grid, val, position):
    # check rows
    for i in range(len(grid[0])):
        if grid[position[0]][i] == val and position[1] != i:
            return False
    
    # check columns
    for i in range(len(grid)):
        if grid[i][position[1]] == val and position[0] != i:
            return False
    
    # check sub_matrix
    start_row = position[0] - position[0] % 3
    start_column = position[1] - position[1] % 3
    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            if grid[i][j] == val and [i, j] != position:
                return False
    
    return True

def find_next_empty_location(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return [i, j]
    return None

def sudoku_solver(grid):
    location = find_next_empty_location(grid)
    if not location:
        return True
    else:
        row, col = location

    for x in range(1, 10):
        if check_board(grid, x, [row, col]):
            grid[row][col] = x
            
            if sudoku_solver(grid):
                return True
            
            grid[row][col] = 0
            
    return False

sudoku_matrix = [
                    [0,0,0,0,0,0,6,8,0],
                    [0,0,0,0,7,3,0,0,9],
                    [3,0,9,0,0,0,0,4,5],
                    [4,9,0,0,0,0,0,0,0],
                    [8,0,3,0,5,0,9,0,2],
                    [0,0,0,0,0,0,0,3,6],
                    [9,6,0,0,0,0,3,0,8],
                    [7,0,0,6,8,0,0,0,0],
                    [0,2,8,0,0,0,0,0,0]
                  ]

print_board(sudoku_matrix)
sudoku_solver(sudoku_matrix)
print_board(sudoku_matrix)

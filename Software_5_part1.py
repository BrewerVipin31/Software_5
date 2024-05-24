def file_input(file_path):
    # Reads a file and converts its lines into a 2D array of characters
    with open(file_path, 'r') as file:
        lines = file.readlines()
    array = [list(line.strip()) for line in lines if line.strip()]
    return array

def moving(row, column, grid, steps, visited):
    # Recursive function to move through the grid and mark accessible cells

    if steps == 0:
        # Base case: no more steps to take
        return

    if (row, column, steps) in visited:
        # If this state has already been visited, return to avoid redundant work
        return

    visited.add((row, column, steps))

    # Move up if possible
    if row > 0 and (grid[row-1][column] == '.' or grid[row-1][column] == '0' or grid[row-1][column] == 'S'):
        if steps == 1:
            grid[row-1][column] = '0'
        moving(row-1, column, grid, steps-1, visited)
    
    # Move down if possible
    if row < len(grid) - 1 and (grid[row+1][column] == '.' or grid[row+1][column] == '0' or grid[row+1][column] == 'S'):
        if steps == 1:
            grid[row+1][column] = '0'
        moving(row+1, column, grid, steps-1, visited)
    
    # Move left if possible
    if column > 0 and (grid[row][column-1] == '.' or grid[row][column-1] == '0' or grid[row][column-1] == 'S'):
        if steps == 1:
            grid[row][column-1] = '0'
        moving(row, column-1, grid, steps-1, visited)
    
    # Move right if possible
    if column < len(grid[0]) - 1 and (grid[row][column+1] == '.' or grid[row][column+1] == '0' or grid[row][column+1] == 'S'):
        if steps == 1:
            grid[row][column+1] = '0'
        moving(row, column+1, grid, steps-1, visited)

if __name__ == "__main__":
    # Define the path to the input file
    file_path = 'puzzle.txt'
    
    # Process the input file to create the grid
    grid = file_input(file_path)
    
    # Find the starting position ('S') in the grid
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                row, column = i, j
                start = [row, column]
                print(start)
                break
        if start:
            break

    # Define the number of steps to take
    steps = 64
    
    # Create a set to track visited states
    visited = set()
    
    # Start moving from the initial position
    moving(row, column, grid, steps, visited)
    
    # Count the number of cells marked as accessible ('0')
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '0':
                count += 1
            print(grid[i][j], end='')
        print()
    
    # Print the total number of accessible locations
    print("Number of possible locations of freedom that can be achieved = %d" % count)

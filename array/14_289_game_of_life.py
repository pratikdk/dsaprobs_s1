def gameOfLife(board):
    # Neighbors array to find 8 neighboring cells for a given cell
    neighbors = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]

    rows = len(board)
    cols = len(board[0])

    # Iterate through board cell by cell.
    for row in range(rows):
        for col in range(cols):

            # For each cell count the number of live neighbors.
            live_neighbors = 0
            for neighbor in neighbors:

                # row and column of the neighboring cell
                r = (row + neighbor[0])
                c = (col + neighbor[1])

                # Check the validity of the neighboring cell and if it was originally a live cell.
                if (r < rows and r >= 0) and (c < cols and c >= 0) and abs(board[r][c]) == 1:
                    live_neighbors += 1

            # Rule 1 or Rule 3
            if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # -1 signifies the cell is now dead but originally was live.
                board[row][col] = -1
            # Rule 4
            if board[row][col] == 0 and live_neighbors == 3:
                # 2 signifies the cell is now live but was originally dead.
                board[row][col] = 2

    # Get the final representation for the newly updated board.
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                board[row][col] = 1
            else:
                board[row][col] = 0


data = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

gameOfLife(data)
print(data)


## Rules:
# - Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# - Any live cell with two or three live neighbors lives on to the next generation.
# - Any live cell with more than three live neighbors dies, as if by over-population..
# - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# [
#   [0,0,0],
#   [1,0,1],
#   [0,1,1],
#   [0,1,0]
# ]

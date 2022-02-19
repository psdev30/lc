class Solution(object):
    def islandPerimeter(self, grid):
        numRows = len(grid)
        numCols = len(grid[0])
        perimeter = 0
        for i, val in enumerate(grid):
            for m, val2 in enumerate(grid[i]):
                if grid[i][m] == 1:
                    if i == 0:
                        up = 0
                    else:
                        up = grid[i - 1][m]
                    if m == 0:
                        left = 0
                    else:
                        left = grid[i][m - 1]
                    if i == numRows - 1:
                        down = 0
                    else:
                        down = grid[i + 1][m]
                    if m == numCols - 1:
                        right = 0
                    else:
                        right = grid[i][m + 1]
                    perimeter += (4 - (up + down + left + right))
        return perimeter
        
                
        
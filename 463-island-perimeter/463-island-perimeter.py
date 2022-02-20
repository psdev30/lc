class Solution(object):
    def islandPerimeter(self, grid):
        #only checking left + up squares
        #time: O(im)
        #space: O(1)
        
        perimeter = 0
        numRows = len(grid)
        numCols = len(grid[0])
        for i in range(numRows):
            for m in range(numCols):
                if grid[i][m] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][m] == 1:
                        perimeter -= 2
                    if m > 0 and grid[i][m - 1] == 1:
                        perimeter -= 2
        return perimeter
        
        
        
        
        
        
        #check all 4 sides
        #time: O(im)
        #space: O(1)
        
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
        
                
        
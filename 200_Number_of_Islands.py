class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_number = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island_number += 1
                    self.DFS(grid,i,j)
                    
        return island_number

    def DFS(self, grid, i ,j):
        if i<0 or j<0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.DFS(grid, i+1,j)
        self.DFS(grid,i,j+1)
        self.DFS(grid,i-1,j)
        self.DFS(grid,i,j-1)
    
def main():
    grid_inputs =[['1','1','1','1','0'],
                 ['1','1','0','1','0'],
                 ['1','1','0','0','0'],
                 ['0','0','0','0','0']]
    
    solution = Solution()
    return solution.numIslands(grid_inputs)

# Question:
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3
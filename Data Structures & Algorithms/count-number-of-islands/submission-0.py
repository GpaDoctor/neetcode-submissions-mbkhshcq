from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Define the 4 cardinal directions (down, up, right, left) to explore neighboring cells
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # Get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        # Helper function for Depth-First Search to sink the current island
        def dfs(r, c):
            # BASE CASE: Stop if we go out of bounds or if the current cell is water ("0")
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            # VISITED: Mark the current land cell as "0" (water) so we don't visit it again.
            # This mutates the grid in-place to save memory instead of using a separate 'visited' set.
            grid[r][c] = "0"
            
            # RECURSIVE STEP: Explore all 4 adjacent directions to sink the rest of the connected island
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Main logic: Iterate through every cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If we encounter land ("1"), it marks the discovery of a new island
                if grid[r][c] == "1":
                    # Run DFS to "sink" (turn to "0") the entire connected body of land
                    dfs(r, c)
                    # Increment our island count since the whole island has now been accounted for
                    islands += 1

        return islands
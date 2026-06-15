class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        ROWS, COLS = len(grid), len(grid[0])
        
        # Keep track of visited cells to avoid infinite loops and duplicate counting
        visit = set()

        # Helper function to perform Depth-First Search (DFS)
        def dfs(r, c):
            # Base Case: If the current coordinates are out of bounds,
            # or the cell is water (0), or we have already visited this cell,
            # it contributes 0 to the island's area.
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            
            # Mark the current land cell as visited
            visit.add((r, c))
            
            # Recursively calculate the area by summing:
            # 1 (for the current cell) + the area of all 4 adjacent directions
            return (1 + dfs(r + 1, c) +  # Down
                        dfs(r - 1, c) +  # Up
                        dfs(r, c + 1) +  # Right
                        dfs(r, c - 1)) # Left

        # Initialize the maximum island area found so far
        max_area = 0
        
        # Traverse every single cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell is land (1) and unvisited, DFS will explore the whole island.
                # If it's water (0) or visited, DFS will instantly return 0.
                # We update max_area if this island is larger than previous ones.
                max_area = max(max_area, dfs(r, c))
                
        return max_area
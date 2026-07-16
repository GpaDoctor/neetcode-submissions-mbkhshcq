from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Get grid dimensions to handle boundary checks
        ROWS, COLS = len(grid), len(grid[0])
        
        # Set to track visited cells so we don't process the same cell twice
        visit = set()
        
        # Queue to facilitate BFS traversal across the grid
        q = deque()

        # Helper function: Validates a cell and schedules it for processing
        def addCell(r, c):
            # Check boundaries: Row or Col cannot be negative, or exceed grid limits
            # Also ensure cell hasn't been visited and is not water (-1)
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return # Skip invalid, visited, or blocked cells
            
            # Mark cell as visited and queue it up for the next wave (layer) of exploration
            visit.add((r, c))
            q.append([r, c])

        # Step 1: Multi-source BFS Initialization
        # Find all treasures (0) in the grid and add them to the queue first.
        # Starting BFS from all treasures simultaneously guarantees we find the
        # shortest path to any treasure for every land cell.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        # Step 2: Traverse outward layer-by-layer
        dist = 0
        while q:
            # Process all cells at the current distance level (wave)
            for i in range(len(q)):
                r, c = q.popleft()
                
                # Update the cell's value with its shortest distance to a treasure
                grid[r][c] = dist
                
                # Expand to all 4 neighboring directions
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            # Increment distance for the next outer layer of cells
            dist += 1
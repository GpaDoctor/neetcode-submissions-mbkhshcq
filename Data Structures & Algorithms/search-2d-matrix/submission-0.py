class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows * cols -1

        while l <= r:
            mid = (l + r)//2

            # divide this and u know which row u on
            row = mid // cols

            # this is harder to understand
            # wrap around logic
            # 0%4=0, 1%4=1, 2%4=2, 3%4=3, 4%4=0, 5%4=1...
            col = mid % cols

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                r = mid - 1
        return False
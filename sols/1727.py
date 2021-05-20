class Solution:
    # Sum continuous stacks of columns (Accepted), O(n * m log m) time, O(1) space
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # If m == 1, should skip the whole looping
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] += matrix[i-1][j]
                else:
                    matrix[i][j] = 0

        res = 0
        # Scan for max across every row
        for i in range(m):
            matrix[i].sort(reverse=True)
            row = matrix[i]
            for j in range(n):
                res = max(res, (j + 1) * row[j])

        return res

    # # Sum continuous stacks of columns (Top Voted), O(n * m log m) time, O(m) space
    # def largestSubmatrix(self, matrix: List[List[int]]) -> int:
    #     ans = 0
    #     for row in range(len(matrix)):
    #         for col in range(len(matrix[0])):
    #             if matrix[row][col] != 0 and row > 0:
    #                 matrix[row][col] += matrix[row - 1][col]

    #         curr = sorted(matrix[row], reverse=True)
    #         for i in range(len(matrix[0])):
    #             ans = max(ans, curr[i] * (i + 1))

    #     return ans

class Solution:
    # Sets DP (Top Voted), O(n^4) time, O(n^3) space
    def minimizeTheDifference(self, mat, target):
        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums}

        return min(abs(target - x) for x in nums)

    # Optimised (Top Voted), O(target * n^2) time, O(target) space
    def minimizeTheDifference(self, mat, target):
        possible_min = sum(min(row) for row in mat)
        if possible_min > target:
            return possible_min - target

        nums = {0}
        for row in mat:
            nums = {x + i for x in row for i in nums if x +
                    i <= 2*target - possible_min}

        return min(abs(target - x) for x in nums)

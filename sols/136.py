from collections import Counter


class Solution(object):
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     # Counter (Hash Table), time O(n), space O(n)
    #     cnt = Counter(nums)
    #     for k, v in cnt.items():
    #         if v == 1:
    #             return k

    # def singleNumber(self, nums):
    #     # Math, time O(n + n) = O(n), space O(n + n) = O(n)
    #     return 2 * sum(set(nums)) - sum(nums)

    def singleNumber(self, nums):
        # Bit Manipulation, time O(n), space O(1)!
        a = 0
        for i in nums:
            a ^= i
        return a

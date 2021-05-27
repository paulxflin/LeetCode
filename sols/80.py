class Solution:
    # # Popping Elements (Accepted), O(n^2) time, O(1) space
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     cur = nums[0]
    #     count = 0
    #     i = 0
    #     while i < len(nums):
    #         if nums[i] == cur:
    #             count += 1
    #         else:
    #             cur = nums[i]
    #             count = 1
    #         if count > 2:
    #             nums.pop(i)
    #             count = 2
    #         else:
    #             i += 1
    #     return i

    # Setting first n elements (Top Voted), O(n) time, O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

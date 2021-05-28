class Solution:
    # # Binary Search on Count (Accepted), O(n (log m + log n)) time
    # # where n = len(position) m = max(position) - min(position), O(1) space
    # def maxDistance(self, position: List[int], m: int) -> int:
    #     def count(d):
    #         cnt = 0
    #         prev = None
    #         for n in position:
    #             if not prev:
    #                 prev = n
    #                 cnt += 1
    #             elif n-prev >= d:
    #                 prev = n
    #                 cnt += 1
    #         return cnt

    #     # Sort position so we can iterate through in linear time afterwards
    #     position.sort()

    #     # Binary search for highest minimum magnetic force.
    #     low = 1
    #     high = position[-1] - position[0]

    #     while low < high:
    #         mid = (low + high + 1) // 2
    #         if count(mid) >= m:
    #             low = mid
    #         else:
    #             high = mid - 1

    #     return low if count(low) >= m else -1

    # Binary Search on Count (Top Voted), O(n (log m + log n)) time, O(1) space
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()

        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l

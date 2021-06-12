import collections
from collections import defaultdict, deque


class Solution(object):
    # # BFS with adjacent and visited dicts (Top Voted), O(n^k) time, O(n^k + n^2) space
    # def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    #     if src == dst:
    #         return 0
    #     d, seen = collections.defaultdict(
    #         list), collections.defaultdict(lambda: float('inf'))
    #     for u, v, p in flights:
    #         d[u] += [(v, p)]

    #     q = [(src, -1, 0)]

    #     while q:
    #         pos, k, cost = q.pop(0)
    #         if pos == dst or k == K:
    #             continue
    #         for nei, p in d[pos]:
    #             if cost + p >= seen[nei]:
    #                 continue
    #             else:
    #                 seen[nei] = cost+p
    #                 q += [(nei, k+1, cost+p)]

    #     return seen[dst] if seen[dst] < float('inf') else -1

    # BFS (Revisit), O(n^k) time, O(n^k + n^2) space
    def finCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        direct_flights, seen = defaultdict(
            lambda: []), defaultdict(lambda: float("inf"))

        for a, b, p in flights:
            direct_flights[a] += [(b, p)]

        q = deque([(src, -1, 0)])

        while q:
            cur, k, price = q.popleft()
            if cur == dst or k == K:
                continue
            for b, p in direct_flights[cur]:
                if price + p >= seen[b]:
                    continue
                else:
                    seen[b] = price + p
                    q.append((b, k+1, price + p))

        return seen[dst] if seen[dst] < float("inf") else -1

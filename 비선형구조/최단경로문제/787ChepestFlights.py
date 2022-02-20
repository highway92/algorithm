from collections import defaultdict
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v,w))
        
        q = [(0, src, k)]

        while q:
            price, node, K = heapq.heappop(q)
            if node == dst:
                return price
            
            if k >= 0:
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(q, (alt, v, k-1))
        return -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for u, v, price in flights:
            graph[u].append((v,price))
            
        queue = [(0, src, k)]
        
        dist = collections.defaultdict(int)
        
        while queue:
            cost, to, k_num = heapq.heappop(queue)
            
            if to == dst:
                return cost
            
            if to not in dist or dist[to] < k_num:
                dist[to] = k_num
                if k_num >= 0:
                    for v, price in graph[to]:
                        alt = cost + price
                        heapq.heappush(queue,(alt, v, k_num -1))
        return -1
        
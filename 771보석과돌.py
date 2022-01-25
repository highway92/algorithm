# 첫 풀이

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        
        for s in jewels:
            dict[s] = 0
            
        for s in stones:
            if s in dict:
                dict[s] += 1
        
        return sum(list(dict.values()))

# defaultdict를 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.defaultdict(int)
        count = 0
        
        for char in stones:
            freq[char] += 1
            
        for char in jewels:
            count += freq[char]
            
        return count

# counter를 이용한 풀이 가장 마음에 든다.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freq = collections.Counter(stones)
        count = 0
        for char in jewels:
            count += freq[char]
            
        return count
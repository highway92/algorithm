from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = Counter(nums)
        return sorted(list(dict.keys()), key = lambda x: - dict[x])[:k]

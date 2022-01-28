from collections import deque
# deque를 이용한 내 풀이
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        q, max = deque(), 0
        for word in s:
            if word not in q: q.append(word)
            else:
                length = len(q)
                max = len(q) if len(q) > max else max
                while q[0] != word and q:
                    q.popleft()
                q.popleft()
                q.append(word)
        return max if max > len(q) else len(q)

# 책의 투포인터를 이용한 풀이
class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start'위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            else: # 최대 부분 문자열 길이 갱신
                max_length = max(max_length, index -  start + 1)
            # 현재 문자의 위치 삽입
            used[char] = index
        return max_length
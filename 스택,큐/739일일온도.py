# 첫번째 풀이는 시간초과... 시간복잡도 O(n) ** 2

def sol(temperatures, result):
    if len(temperatures) == 1:
        result.append(0)
        return result
    
    cur_temp = temperatures[0]
    temperatures = temperatures[1:]

    for idx, val in enumerate(temperatures):
        if val > cur_temp:
            result.append(idx+1)
            break
    else:
        result.append(0)
    return sol(temperatures, result)         



# 책을 보고 푼 코드 시간복잡도 O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for idx, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = idx - last
            stack.append(idx)
        
        return answer
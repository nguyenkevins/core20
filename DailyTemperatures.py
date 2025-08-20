class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = [] # [temp, index]
        result = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while s and s[-1][0] < temperatures[i]:
                result[s[-1][1]] = i - s[-1][1]
                s.pop()
            s.append([temperatures[i], i])
        return result

# 第 N 个泰波那契数

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        return self.tribonacci(n-1)*2 - self.tribonacci(n-4)

print(Solution().tribonacci(5))

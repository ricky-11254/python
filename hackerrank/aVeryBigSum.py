class Solution:
    def __init__(self, n):
        self.n = n
        self.ar = []

    def aVeryBigSum(self):
        value = input().split()
        for i in range(self.n):
            self.ar.append(int(value[i]))
        return sum(self.ar)

n = int(input())
solution = Solution(n)
print(solution.aVeryBigSum())
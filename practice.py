class Solution:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.arr = []

    def two2_array(self):
        for i in range(self.rows):
            value = input().split()
            row = []
            for j in range(self.cols):
                row.append(value[j])
            self.arr.append(row)
        return self.arr

rows = int(input())
cols = int(input())
solution = Solution(rows, cols)
print(solution.two2_array())

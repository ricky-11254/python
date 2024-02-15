from array import array

class Solution:
    def __init__(self, n):
        self.n = n
        self.A = array('i')

    def input_array(self):
        values = input().split()
        for value in values:
            self.A.append(int(value))

    def find_second_largest(self):
        sorted_array = sorted(self.A, reverse=True)
        if len(sorted_array) < 2:
            return None
        return sorted_array[1]

n = int(input())
solution = Solution(n)
solution.input_array()
second_largest = solution.find_second_largest()
print(second_largest)


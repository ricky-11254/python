from array import array

class Solution:
    def __init__ (self):
        self.a = array('i')
        self.b = array('i')
    
    def compareTriplets(self):
        value_a = input().split()
        for i in range(3):
            self.a.append(int(value_a[i]))

        value_b = input().split()
        for i in range(3):
            self.b.append(int(value_b[i]))

        points_a = 0
        points_b = 0

        for i in range(3):
            if self.a[i] >self.b[i]:
                points_a += 1
            elif self.a[i] < self.b[i]:
                points_b += 1
        return points_a, points_b

solution = Solution()
points_a, points_b = (solution.compareTriplets())
print(f"{points_a} {points_b}")

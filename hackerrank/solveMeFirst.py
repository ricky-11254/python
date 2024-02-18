class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def return_sum(self, a, b):
        sum = self.a + self.b
        return sum

a = int(input())
b = int(input())
sum = Sum(a, b)
answer = sum.return_sum(a, b)
print(answer)

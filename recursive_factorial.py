class Recursion:
    def __init__(self, n):
        self.n = n
    def factorial(n):
        if n==0:
            return 1
        else:
            return n * factorial(n-1)

n = input()
recursion = Recursion(n)
recursion.factorial()
print(factorial)

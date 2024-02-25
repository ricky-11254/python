class BubbleSort:
    def __init__(self, n):
        self.n = n
        self.arr = []

    def bubble_sort(self):
        value = input().split()
        for i in range(self.n):
            self.arr.append(int(value[i]))
        for i in range(self.n):
            for j in range(self.n-1):
                if(self.arr[j] > self.arr[j+1]):
                   self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
            return self.arr

n = int(input())
bubblesort = BubbleSort(n)
print(bubblesort.bubble_sort())


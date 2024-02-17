class Input:
    def __init__(self, size):
        self.size = size
        self.goat = []

    def input_values(self):
        value = int(input())
        for i in range(self.size):
            self.goat.append(int(value))

size = int(input())
what = Input(size)
what.input_values()
print(what.goat)

from array import array

class ArrayInput:
    def __init__(self, size):
        self.size = size
        self.my_array = array('i')

    def input_values(self):
        values = input().split()
        for i in range(self.size):
            self.my_array.append(int(value))

size = int(input())
array_input = ArrayInput(size)
array_input.input_values()
print(array_input.my_array)

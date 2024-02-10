from array import array

my_array = array('i')

size = int(input())
for i in range(size):
    value = int(input())
    my_array.append(value)
print(my_array)

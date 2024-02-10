def count_bits(n):
    int number
    number = input()
    while number > 0:
        rem = number % 2
        if rem != 0:
            binary = rem * 2
        else:
            binary = 0
    print(binary)
    return
array = [7, 9, 5, 3, 1, 2, 4, 6, 8, 7]
numchange = 0
InnerLoop = 0
OuterLoop = 0
TotalNumberOfLoops = 10

while OuterLoop < TotalNumberOfLoops:
    InnerLoop = OuterLoop + 1
    while InnerLoop < TotalNumberOfLoops:
        if array[OuterLoop] < array[InnerLoop]:
            numchange = array[InnerLoop]
            array[OuterLoop] = array[InnerLoop]
            array[InnerLoop] = numchange

        InnerLoop = InnerLoop + 1

print(array)
OuterLoop = OuterLoop + 1
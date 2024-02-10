array = [7, 9, 5, 3, 1, 2, 4, 6, 8, 7]  # Initialize an array to be sorted
numchange = 0  # Temporary variable for swapping
TotalNumberofLoops = 10  # Total number of elements in the array
OuterLoop = 0  # Outer loop counter
InnerLoop = 0  # Inner loop counter

while OuterLoop < TotalNumberofLoops:  # Outer loop to iterate through the array
  InnerLoop = OuterLoop + 1  # Initialize InnerLoop one position ahead of OuterLoop
  while InnerLoop < TotalNumberofLoops:  # Inner loop to compare and swap elements
    if array[OuterLoop] < array[InnerLoop]:  # Compare two adjacent elements
      numchange = array[InnerLoop]  # Store the larger element in numchange
      array[OuterLoop] = array[InnerLoop]  # Swap the elements
      array[InnerLoop] = numchange  # Set the smaller element to the current InnerLoop

    InnerLoop = InnerLoop + 1  # Move to the next element in the inner loop

  print(array)  # Print the array after each pass (for visualization)
  OuterLoop = OuterLoop + 1  # Move to the next element in the outer loop

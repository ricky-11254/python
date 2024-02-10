def longestword(sen):
    words = sen.split()  # Split the input sentence into words
    longest = max(words, key=len)  # Find the word with the maximum length
    return longest

input_sentence = input("Enter a sentence: ")
result = longestword(input_sentence)
print(f"The longest word in the sentence is: {result}")

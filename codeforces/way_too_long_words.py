class Solution:

    def __init__(self, word):
        self.word = word

    def shorten_word(self):
        return self.word[0] + self.word.len -2 + self.word [-1]

word = input()
solution = Solution(word)
shorten_word = solution.shorten_word()
print(shorten_word)
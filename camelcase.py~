class Solution:
    def __init__(self, s):
        self.s = s

    def count_words(self):
        if not self.s:
            return 0

        count = 1
        for i in range(1, len(self.s)):
            if self.s[i].isupper() and self.s[i-1].islower():
                count += 1

        return count

s = input()            
word_count = Solution(s).count_words()
print(word_count)

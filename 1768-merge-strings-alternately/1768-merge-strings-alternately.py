class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        new_word = ''

        for i in range(max(len1, len2)):
            if i < len1:
                new_word += word1[i]
            if i < len2:
                new_word += word2[i]
        return new_word

        
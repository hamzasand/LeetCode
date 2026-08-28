class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in range(1,len(strs)):

            while not strs[word].startswith(prefix):

                prefix = prefix[:-1]

                if prefix == "":
                    return ""
        return prefix
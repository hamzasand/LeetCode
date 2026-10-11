class Solution:
    def reverseWords(self, s: str) -> str:
        n = len(s)

        stack = deque()
        i=0

        while i<n:
            if s[i] ==' ':
                i +=1
                continue
            else:
                word = ""
                while i<n and s[i] != ' ':
                    word += s[i]
                    i +=1
                stack.appendleft(word)
        
        return " ".join(stack)
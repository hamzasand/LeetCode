class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        rev_num = 0
        while x > 0:
            rem = x % 10
            rev_num = rev_num * 10 + rem
            x = x // 10
        if rev_num == original:
            return True
        else:
            return False
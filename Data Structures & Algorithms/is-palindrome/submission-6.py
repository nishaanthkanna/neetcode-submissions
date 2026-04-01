class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            # if non-alphanumeric ignore
            while l < len(s) and (not s[l].isalnum()):
                l += 1
            while r >= 0 and (not s[r].isalnum()):
                r -= 1
            if l >= r:
                break
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
            
        
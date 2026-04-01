class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dup = set()
        L = 0
        R = 1
        dup.add(s[L])
        max_l = 1
        while R < len(s):
            if s[R] not in dup:
                max_l = max(max_l, (R-L)+1)
                dup.add(s[R])
                R += 1
            else:
                dup.remove(s[L])
                L += 1
        
        return max_l


        
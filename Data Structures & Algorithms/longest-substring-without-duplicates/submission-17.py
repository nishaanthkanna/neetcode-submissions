# Pointers with a hashset
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        if len(s) <= 1:
            return len(s)
        l = 0
        r = 1
        hashset = set(s[l])
        while r < len(s):
            if s[r] in hashset:
                # duplicate, remove s[l] from hashset, so reduce window size
                #longest = max(longest, len(hashset))
                hashset.remove(s[l])
                l += 1
            else:
                hashset.add(s[r])
                r += 1
            longest = max(longest, len(hashset))
        
        return longest
            
        
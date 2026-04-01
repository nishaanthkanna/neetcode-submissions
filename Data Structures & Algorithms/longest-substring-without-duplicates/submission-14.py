# Brute force solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # check first case outside of the loop
        if len(set(s)) == len(s):
            return len(s)

        window_size = len(s)

        while window_size > 1:
            print(len(s))
            print(window_size)
            for i in range((len(s) - window_size)+1):
                sub_string = s[i:i+window_size]
                if len(set(sub_string)) == len(sub_string):
                    # doesnt contain duplicates
                    return len(sub_string)
            window_size -= 1
        
        return window_size

        
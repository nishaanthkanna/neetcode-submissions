
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two options
        # sort two strings and compare. TC O(2*(n log n) + n)
        # store one string as a hashmap occurence. 
        # compare that with the second one. TC (o(N)+o(N))
        hMap = {}
        for c in s:
            hMap[c] = hMap.get(c, 0) + 1

        for c in t:
            if c not in hMap:
                return False
            else:
                hMap[c] -= 1

        # if hMap is all zero then return True
        for k,v in hMap.items():
            if v != 0:
                return False
        return True

        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            charArray = [0]*26
            for c in s:
                val = ord(c) - ord('a')
                charArray[val] += 1
            hashMap[tuple(charArray)].append(s)

        # print(hashMap) 

        return [st for _, st in hashMap.items()]
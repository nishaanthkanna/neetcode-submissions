class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # since need to group, enough if we have to check which group a string belongs too
        #  option 1: sort each string, use the sorted string as key and matching strings as value:
        # TC: O(N*M log M), SC: O(k+M)
        # option 2: create a 26 character tuple, store it as key and validate strings with it.
        # TC: O(N*m), SC: O(k+M)
        # confirmed if lowercase

        if len(strs) < 2:
            return [strs]

        def return_tuple_format(s: str) -> tuple:
            char_list = [0 for _ in range(26)]
            for c in s:
                char_list[ord(c)-97] += 1
            return tuple(char_list)

        hMap = {}
        for s in strs:
            char_tuple = return_tuple_format(s)
            if char_tuple in hMap:
                hMap[char_tuple].append(s)
            else:
                hMap[char_tuple] = [s]
        
        return [v for k, v in hMap.items()]

        
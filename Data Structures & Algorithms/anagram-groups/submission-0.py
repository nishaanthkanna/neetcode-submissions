class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for a in strs:
            temp = "".join(sorted(a))
            hashMap[temp].append(a)
        return [v for _, v in hashMap.items()]

        
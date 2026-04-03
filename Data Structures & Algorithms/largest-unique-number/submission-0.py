class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashMap = {}
        max_i = -1
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] += 1
        
        for k, v in hashMap.items():
            if v == 1:
                max_i = max(max_i, k)
        return max_i
        
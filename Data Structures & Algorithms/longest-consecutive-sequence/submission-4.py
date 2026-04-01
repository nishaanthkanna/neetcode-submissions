class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap = {}
        for i in nums:
            if i-1 in hashMap:
                hashMap[i] = 1
            else:
                hashMap[i] = 0
        max_len = 0
        for k, v in hashMap.items():
            tmp_len = 0
            if v == 0:
                tmp = k
                while tmp in hashMap:
                    tmp_len += 1
                    tmp += 1
                max_len = max(max_len, tmp_len)
        
        return max_len

        
        
        
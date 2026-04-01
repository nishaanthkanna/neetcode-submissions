class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        seq = {}
        for i in hashset:
            tmp = i-1
            if tmp not in hashset:
                seq[i] = 0
        ans = 0
        print(seq)
        for k in seq.keys():
            counter = 0
            while True:
                tmp = k + counter 
                if tmp in hashset:
                    counter += 1
                else:
                    ans = max(ans, counter)
                    counter = 0
                    break
        return ans
                


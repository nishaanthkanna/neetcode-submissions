class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        # sort hashMap based on values
        # algorithm the groups number based on frequency??? -> bucket sort
        sort = sorted(hashMap.items(), key = lambda x : x[1], reverse=True)
        output = []
        for i in range(k):
            output.append(sort[i][0])
        return output
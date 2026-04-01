class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        bucket = [[] for _ in range(len(nums)+1)]
        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1
        
        for k1, v in hashMap.items():
            bucket[v].append(k1)
        output = []
        print(bucket)
        for i in range(len(bucket) - 1, -1, -1):
            if k == 0:
                return output
            if len(bucket[i]) > 0:
                output.extend(bucket[i])
                k -= len(bucket[i])
        return output

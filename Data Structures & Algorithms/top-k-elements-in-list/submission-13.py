class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # store frequency counter of the nums in a dict, sort the dict, pick top k
        # TC: o(N+k log k) SC: O(k)

        hash_map = {}

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        
        # sort the dict by value
        hash_map = dict(sorted(hash_map.items(), key=lambda x: x[1], reverse=True))

        output = []
        for key, val in hash_map.items():
            if k:
                output.append(key)
                k -= 1
        return  output
        
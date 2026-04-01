class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        hashMap = defaultdict(list)
        for i, v in enumerate(nums):
            hashMap[v].append(i)

        output = set()
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                vi = nums[i]
                vj = nums[j]
                vk = -(vi + vj)
                if vk in hashMap:
                    # check if picked distinct indices
                    for m in hashMap[vk]:
                        if m != i and m != j:
                            output.add(tuple(sorted([vi, vj, vk])))
                j += 1
            i += 1
        
        return [list(i) for i in output]


        
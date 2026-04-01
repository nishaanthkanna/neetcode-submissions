class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = defaultdict(list)
        # first build the hashmap
        for i, value in enumerate(nums):
            hashMap[value].append(i)
        
        for i in nums:
            diff = target - i
            # check not to select the same item
            if diff == i and len(hashMap[diff]) > 1:
                # return the indices
                return hashMap[diff]
            # make sure the duplicate element is not selected
            if diff in hashMap:
                ansI = hashMap[i][0]
                ansJ = hashMap[diff][0]
                if ansI == ansJ:
                    continue
                if ansI < ansJ:
                    return [ansI, ansJ]
                else:
                    return [ansJ, ansI]
                

                

        
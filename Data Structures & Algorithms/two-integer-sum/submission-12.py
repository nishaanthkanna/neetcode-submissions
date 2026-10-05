from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if you need to avoid rechecking the array/string hashmap them

        #  store the nums in a hasMap with value as key and position as index
        hMap = defaultdict(list)
        for i, v in enumerate(nums):
            hMap[v].append(i)
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hMap:
                diff_i = hMap.get(diff)
                if diff_i[0] != i:
                    if diff == v:
                        return diff_i
                    else:
                        if i < diff_i[0]:
                            return [i, diff_i[0]]
                        else:
                            return [diff_i[0], i]


        
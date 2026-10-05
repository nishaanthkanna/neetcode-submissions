from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # if you need to avoid rechecking the array/string hashmap them

        #  store the nums in a hasMap with value as key and position as index
        hMap = {}
        for i, v in enumerate(nums):
            hMap[v] = i
        
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hMap and hMap[diff] != i:
                return [i, hMap[diff]]



        
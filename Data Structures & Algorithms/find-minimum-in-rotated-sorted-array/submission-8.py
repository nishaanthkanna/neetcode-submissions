class Solution:
    def findMin(self, nums: List[int]) -> int:

        L = 0
        R = len(nums) - 1

        while (R-L) > 0:
            m = (R-L) // 2
            m += L
            if nums[m] < nums[L]:
                R = m
            elif nums[m] > nums[R]:
                L = m + 1
            else: # if not rotated
                return nums[L]
        
        return nums[L]
        


        
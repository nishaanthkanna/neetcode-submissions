class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return nums[0]
            return nums[1]

        m = (len(nums) // 2)
        # answer might be in right
        if nums[m] < nums[0]:
            return self.findMin(nums[:m+1])
        elif nums[m] > nums[-1]:
            return self.findMin(nums[m:])
        else: # if not rotated
            # if nums[m] > nums[0] and nums[m] < nums[-1]:
                return nums[0]

        
        return ans


        
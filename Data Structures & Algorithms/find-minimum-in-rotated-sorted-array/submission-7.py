class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        m = len(nums) // 2
        if nums[m] < nums[0]:
            return self.findMin(nums[1:m+1])
        elif nums[m] > nums[-1]:
            return self.findMin(nums[m+1:])
        else: # if not rotated
            return nums[0]


        
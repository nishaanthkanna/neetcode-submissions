class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 2)

        left[0] = 1
        right[0] = 1
        right[n+1] = 1
        leftS = 1
        rightS = 1
        for i, v in enumerate(nums):
            leftS *= v
            left[i+1] = leftS

        for i in range(len(nums) - 1, -1, -1):
            rightS *= nums[i]
            right[i+1] = rightS

        output = []
        for i in range(1, len(nums)+1):
            output.append(left[i-1]*right[i+1])
        
        return output
        

        
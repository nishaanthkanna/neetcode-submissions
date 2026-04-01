class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        from copy import copy
        ans = copy(nums)
        for i in nums:
            ans.append(i)

        return ans
        
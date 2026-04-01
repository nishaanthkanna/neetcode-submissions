class Solution:
    def search(self, nums: List[int], target: int) -> int:

        L = 0
        R = len(nums) - 1
        output = -1
        while (R-L) > 1:
            m = (R - L) // 2
            m += L
            # check if array rotated less than half
            if nums[m] < nums[L]:
                # search in right half
                if target > nums[m] and target <= nums[R]:
                    L = m + 1
                # search in left half
                else:
                    R = m
            elif nums[m] > nums[R]:
                # search in left half
                if target >= nums[L] and target < nums[m]:
                    R = m
                else:
                    L = m + 1
            # Already sorted
            else:
                # search in left
                if target < nums[m]: 
                    R = m
                elif target > nums[m]:
                    L = m + 1
                else:
                    L = R = m
        
        if nums[L] == target:
            output = L
        elif nums[R] == target:
            output = R

        return output

        
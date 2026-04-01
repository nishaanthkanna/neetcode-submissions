class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0 for _ in nums]
        total_product = 1
        zero_index = []
        for i, n in enumerate(nums):
            if n != 0:
                total_product *= n
            else:
                zero_index.append(i)

        # special case of zero
        if len(zero_index) == 0:
            for i, n in enumerate(nums):
                output[i] = total_product//n
        elif len(zero_index) == 1:
            output[zero_index[0]] = total_product
        else:
            return output
        

        return output
        
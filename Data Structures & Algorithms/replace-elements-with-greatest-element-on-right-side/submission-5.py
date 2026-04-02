class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 2
        output = [0] * (i+2)
        output[i+1] = -1
        max_i = 0
        while i >= 0:
            max_i = max(max_i, arr[i+1])
            output[i] = max_i
            i -= 1
        return output

        
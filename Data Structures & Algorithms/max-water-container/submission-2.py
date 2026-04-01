class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1
        while j > i:
            vi = heights[i]
            vj = heights[j]

            area = (j - i) * min(vi, vj)
            print(i, j, area)
            max_area = max(area, max_area)
            # vpi = heights[i+1] - vi
            # vpj = heights[j-1] - vj
            if vi < vj:
                i += 1
            else:
                j -= 1
            
        
        return max_area



        
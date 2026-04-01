class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            tmp = (j-i) * min(heights[i], heights[j])
            area = max(area, tmp)
            if heights[i] < heights[j]:
                i+=1
            else:
                j-=1
        
        return area
        
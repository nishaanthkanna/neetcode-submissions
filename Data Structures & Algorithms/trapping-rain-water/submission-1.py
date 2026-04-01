class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        i = 0
        if len(height) <= 1:
            return total_area
        # only for the first section
        while height[i] == 0 and i < len(height):
            i+=1
        
        # if all empty
        if i == len(height):
            return total_area
        j = i+ 1
        while j < len(height):
            
            sub_height = []
            while j < len(height) :
                if height[j] >= height[i]:
                    break
                sub_height.append(height[j])
                j+=1
            # if reached end of array without discovering the second tallest. pick first max of the height within the sub_bars
            # another case, actually reached end and there is between bars that could be discovered
            # if reached end and the sub_height is all decreasign then water cannot be trapped
            if j == len(height):
                a = 0
                b = 1
                decreasing = True
                while b < len(sub_height):
                    if sub_height[b] > sub_height[a]:
                        decreasing = False
                        break
                    a += 1
                    b += 1
                if decreasing: #can exit loop
                    return total_area
                max_sub_height = max(sub_height)
                msh_i = sub_height.index(max_sub_height)
                j = i + msh_i + 1
                # compute subarea
                subarea = sum(sub_height[:msh_i])
            else:
                subarea = sum(sub_height)
            
            print(sub_height)
            print(subarea)
            print(j)
            width = j - i - 1
            max_poss_area = width * min(height[i] , height[j])
            total_area += max_poss_area - subarea

            i = j
            j = i+ 1
        return total_area

        
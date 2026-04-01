# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # split arrays to size one
        # then sort them while merging
        # why efficient? since we are merging sorted sub arrays the number of comparisons could be less
        if len(pairs) <= 1:
            return pairs

        middle = len(pairs)  // 2
        leftArray = pairs[0 : middle]
        rightArray = pairs[middle:]

        leftArray = self.mergeSort(leftArray)
        rightArray = self.mergeSort(rightArray)

        return self.merge(leftArray, rightArray)
    
    def merge(self, leftArray: List[Pair], rightArray: List[Pair]) -> List[Pair]:

        newArray = []
        # points to two arrays
        l = 0
        r = 0
        while l < len(leftArray) and r < len(rightArray):
            
            if leftArray[l].key < rightArray[r].key:
                newArray.append(leftArray[l])
                l += 1
            elif leftArray[l].key > rightArray[r].key:
                newArray.append(rightArray[r])
                r += 1
            # if both are equal, maintain order but using the element from the left array
            else:
                newArray.append(leftArray[l])
                l += 1

        # if any one of the pointers didnot reach the end, insert the other subarray
        for i in leftArray[l:]:
            newArray.append(i)
        for j in rightArray[r:]:
            newArray.append(j)
        
        return newArray




        

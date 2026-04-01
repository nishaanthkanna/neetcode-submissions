class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = {}
        for i in nums:
            if i not in hashSet:
                hashSet[i] = 0
            else:
                return True

        return False
        
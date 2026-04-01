class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = defaultdict(list)

        for i, v in enumerate(nums):
            hashMap[v].append(i)
        for i, v in enumerate(nums):
            diff = target - v
            index = hashMap.get(diff, [])
            if len(index) != 0:
                # if v and diff are the same (duplicate), return the entire value
                if diff == v and len(index) == 2:
                    return index
                elif diff != v:
                    j = index[0]
                    return [i, j] if i < j else [j, i]
        


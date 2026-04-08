class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen= {}
        for i,x in enumerate(nums):
            comp = target - x
            if comp in seen:
                j = seen[comp]
                return [min(i,j), max(i,j)]
            seen[x] = i
        return[]
            
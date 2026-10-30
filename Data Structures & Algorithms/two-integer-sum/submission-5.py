class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, n in enumerate(nums):
            idx = ht.get(target - n, -1)
            if idx != -1:
                return [idx, i]
            ht[n] = i
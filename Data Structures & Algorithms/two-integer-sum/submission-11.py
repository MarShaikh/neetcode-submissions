class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in hash_map:
                return [hash_map[k], i]
            hash_map[n] = i
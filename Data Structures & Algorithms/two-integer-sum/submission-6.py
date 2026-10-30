class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        
        for i, n in enumerate(nums):
            r = target - n
            if r in hash_map:
                return [hash_map[r], i]
            hash_map[n] = i

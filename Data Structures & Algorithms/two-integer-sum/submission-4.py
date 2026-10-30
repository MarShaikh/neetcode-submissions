class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            idx = hmap.get((target - nums[i]), -1)
            if idx != -1:
                return [idx, i]
            hmap[nums[i]] = i
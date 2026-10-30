class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            hmap[nums[i]] = i
        
        for i in range(len(nums)):
            f = target - nums[i]
            
            if hmap.get(f, 0) != 0:
                if i != hmap[f]:
                    return [i, hmap[f]]
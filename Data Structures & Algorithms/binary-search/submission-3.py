import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target) # built-in function
        return index if index < len(nums) and nums[index] == target else -1
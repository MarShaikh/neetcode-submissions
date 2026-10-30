class Solution:
    def search(self, nums: List[int], target: int) -> int:
        p, q = 0, len(nums) - 1
        
        while p <= q:
            mid = p + ((q - p) // 2)

            if nums[mid] < target:
                p = mid + 1
            elif nums[mid] > target:
                q = mid - 1
            else:
                return mid
        
        return -1

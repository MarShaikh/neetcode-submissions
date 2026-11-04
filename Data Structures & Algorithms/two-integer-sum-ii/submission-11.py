class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        for i in range(len(numbers)):
            k = target - numbers[l] - numbers[r]
            if k < 0 :
                r -= 1
            elif k > 0:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []
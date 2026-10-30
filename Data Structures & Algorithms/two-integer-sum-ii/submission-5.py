class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if target - numbers[l] > numbers[r]:
                l += 1
            elif target - numbers[l] < numbers[r]:
                r -= 1
            else: 
                return [l + 1, r + 1]



"""
increasing order sorted array

return two numbers [idx1, idx2] and idx1 < idx2; idx1 != idx2

ip: [1 2 3 4] target = 3
op: [1 2]

ip: [3 4 5 6] target 10
op: [4 6]

10 - 3 =>
7 > 6
"""
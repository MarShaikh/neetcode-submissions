class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            temp = target - numbers[j]

            if temp == numbers[i]:
                return [i + 1, j + 1]
            
            if temp > numbers[i]:
                i = i + 1
            elif temp < numbers[i]:
                j = j - 1
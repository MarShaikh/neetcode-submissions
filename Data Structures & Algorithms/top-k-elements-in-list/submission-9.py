class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map_counts = {}
        count_list = [[] for _ in range(len(nums) + 1)]

        # get counts of elements in the array
        for n in nums:
            hash_map_counts[n] = 1 + hash_map_counts.get(n, 0)

        # put these counts in the count_list
        for key, value in hash_map_counts.items():
            count_list[value].append(key)

        # get the values from the count array
        res = []
        for count in reversed(count_list):
            for n in count:
                res.append(n)
                if len(res) == k:
                    return res

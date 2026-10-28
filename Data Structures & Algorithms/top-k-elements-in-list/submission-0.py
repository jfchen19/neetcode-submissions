class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        freq = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            groups[num] = groups.get(num, 0) + 1

        for num, count in groups.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return []
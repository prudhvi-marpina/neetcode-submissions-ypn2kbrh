class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        frequency = {}
        for x in nums:
            if x in frequency:
                frequency[x] += 1
            else:
                frequency[x] = 1
        
        buckets = [[]for _ in range(n+1)]
        for val, f in frequency.items():
            buckets[f].append(val)
        
        res = []
        for f in range(n, 0, -1):
            for val in buckets[f]:
                res.append(val)
                if len(res) == k:
                    return res
        return res

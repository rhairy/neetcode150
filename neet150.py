class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            i = i + 1
        return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else:
            return False

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 1
        while i < len(nums):
            j = i - 1
            while j >= 0:
                if nums[i] + nums[j] == target:
                    return sorted([i, j])
                j = j - 1
            i = i + 1

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for i in strs:
            original = i
            ref = ''.join(sorted(i))
            if ref in res:
                res[ref].append(original)
            else:
                res[ref] = [original]
        return list(res.values())

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] = d[i] + 1
        res = sorted(d.items(), key=lambda tup: tup[1], reverse=True)
        i = 0
        out = []
        for i in range(k):
            out.append(res[i][0])
        return out

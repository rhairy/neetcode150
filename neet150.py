class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        i = 0
        while i < (len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
            i = i + 1
        return False
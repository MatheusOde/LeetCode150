class Solution(object):
    def removeDuplicates(self, nums):
        result = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                result.append(nums[i])
        nums[:] = result[:]
        return len(nums)

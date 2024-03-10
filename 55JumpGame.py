class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        currentIndex = 0
        stops = 0
        while currentIndex+1 < len(nums):
            if nums[currentIndex] == 0 and i == 0:
                return False
            if nums[currentIndex] > i:
                i = nums[currentIndex]
                stops += 1
            i -= 1
            currentIndex += 1
        return stops


def main():
    nums = [2, 3, 0, 1, 4]

    solution_instance = Solution()
    print(solution_instance.canJump(nums))
    print(nums)


if __name__ == '__main__':
    main()

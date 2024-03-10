class Solution(object):
    def removeDuplicates(self, nums):
        d_count = 0
        i = 0
        j = len(nums)
        while i < j:
            if nums[i] == nums[i - 1] and i >= 1:
                d_count += 1
                if d_count == 2:
                    nums.pop(i)
                    j -= 1
                    i -= 1
                    d_count = 1
            else:
                d_count = 0
            i += 1
            if i == j:
                return len(nums)


def main():
    nums = [1, 1, 1, 2, 2, 3]

    solution_instance = Solution()
    print(solution_instance.removeDuplicates(nums))
    print(nums)


if __name__ == '__main__':
    main()

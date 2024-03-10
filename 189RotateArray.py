class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        index_troca = len(nums) - k

        nums[:] = nums[index_troca:] + nums[:index_troca]

        return nums


def main():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 8

    solution_instance = Solution()
    print(solution_instance.rotate(nums, k))
    print(nums)


if __name__ == '__main__':
    main()

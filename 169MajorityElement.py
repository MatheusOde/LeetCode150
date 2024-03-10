class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_number = None
        majority = int(len(nums)/2) + 1
        count = {}
        for num in nums:
            try:
                count[num] += 1
            except KeyError:
                count[num] = 1

            if count[num] >= majority:
                majority_number = num

        return majority_number


def main():
    nums = [3, 3, 4]

    solution_instance = Solution()
    print(solution_instance.majorityElement(nums))
    print(nums)


if __name__ == '__main__':
    main()

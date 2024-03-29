class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = [1] * len(nums)
        index = 0
        multiplier = 1
        for i in range(len(nums)):
            multiplier *= nums[i]
            
        
        while index < len(nums):
            for i in range(0, index):
                array[index] *= nums[i]

            for i in range(index+1, len(nums)):
                array[index] *= nums[i]

            index += 1
        return array


def main():
    nums = [1,2 ,3, 4]
    solution_instance = Solution()
    print("Solution instance: ", solution_instance.productExceptSelf(nums))


if __name__ == '__main__':
    main()

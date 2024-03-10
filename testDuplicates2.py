import unittest
import removeDuplicates2 as removeDuplicates


class TestDuplicatesRemoved(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        expectedNums = [1, 1, 2, 2, 3]

        result = removeDuplicates.Solution.removeDuplicates(self, nums)
        self.assertEqual(result, len(expectedNums))
        for i in range(result):
            assert nums[i] == expectedNums[i]

    def test_example_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expectedNums = [0, 0, 1, 1, 2, 3, 3]

        result = removeDuplicates.Solution.removeDuplicates(self, nums)
        self.assertEqual(result, len(expectedNums))
        for i in range(result):
            assert nums[i] == expectedNums[i]


if __name__ == '__main__':
    unittest.main()

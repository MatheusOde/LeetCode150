class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        low = min(citations)
        high = max(citations)
        mid = (low + high) // 2
        mid += 1
        while low <= high:
            print("mid ", mid)
            print("high ", high)
            print("low ", low)

            count = 0
            passH = False
            # Does it pass H-Index?
            for num in citations:
                if num >= mid:
                    count += 1
                    if count >= mid:
                        passH = True
                        break

            print("passH: ", passH)
            if passH and mid > low:
                low = mid
            else:
                high = mid

            if high == low:
                if high > len(citations):
                    return len(citations)
                return low
            print("low: ", low)
            mid = (low + high) // 2

        return -1


def main():
    nums = [100]
    solution_instance = Solution()
    print(solution_instance.hIndex(nums))
    print(nums)


if __name__ == '__main__':
    main()

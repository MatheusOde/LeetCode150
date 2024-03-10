class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()

        low = min(citations)
        high = max(citations)

        while low <= high:
            mid = (low + high) // 2
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

            if passH and mid > low:
                low = mid
            else:
                high = mid

            if high == low:
                return low
            print("low: ", low)
            # count = sum(1 for num in citations if num == mid)

            # if count >= x:
            #     return mid
            # elif count < x:
            #     low = mid + 1
            # else:
            #     high = mid - 1

        return -1


def main():
    nums = [1, 3, 1]

    solution_instance = Solution()
    print(solution_instance.hIndex(nums))
    print(nums)


if __name__ == '__main__':
    main()

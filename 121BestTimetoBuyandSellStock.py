class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        
        """
        minbuy = float('inf')
        maxsell = 0
        for i in range(0, len(prices)):
            minbuy = min(minbuy, prices[i])
            maxsell = max(maxsell, prices[i]-minbuy)
        return maxsell


def main():
    prices = [7, 1, 5, 3, 6, 4]

    solution_instance = Solution()
    print(solution_instance.maxProfit(prices))
    print(prices)


if __name__ == '__main__':
    main()

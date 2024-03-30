class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy_distribution = [1] * len(ratings)
        i = 0
        for i in range(len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_distribution[i] += 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candy_distribution[i] += 1
            if ratings[i] - ratings[i+1] == 2:
                ratings[i] = 2

        print(candy_distribution)
        return sum(candy_distribution)


def main():
    ratings = [1, 3, 2, 2, 1]
    solution_instance = Solution()
    print("Solution instance: ", solution_instance.candy(ratings))


if __name__ == '__main__':
    main()

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        stops = len(cost)
        total_gas = 0
        counter = 0
        stop = 0
        start = 0
        end = stops
        while stop <= stops:
            total_gas += gas[stop]
            total_gas -= cost[stop]
            counter += 1
            if total_gas <= 0 and stop < stops:
                start += 1
                end = start + stops
                stop = start
                counter = 0
                total_gas = 0
            if stop == stops - 1:
                stop = 0
            if counter == end:
                return start
            if start >= stops:
                return -1


def main():
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    solution_instance = Solution()
    print("Solution instance: ", solution_instance.canCompleteCircuit(gas, cost))


if __name__ == '__main__':
    main()

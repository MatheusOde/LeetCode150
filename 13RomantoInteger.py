class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i, char in enumerate(s):
            if char == 'M':
                sum += 1000
            elif char == 'D':
                sum += 500
            elif char == 'C':
                sum += 100
                if i < len(s) - 1 and (s[i+1] == 'M' or s[i+1] == 'D'):
                    sum -= 200
            elif char == 'L':
                sum += 50
            elif char == 'X':
                sum += 10
                if i < len(s) - 1 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    sum -= 20
            elif char == 'V':
                sum += 5
            elif char == 'I':
                sum += 1
                if i < len(s) - 1 and (s[i+1] == 'X' or s[i+1] == 'V'):
                    sum -= 2
        return sum


def main():
    s = "MCMXCIV"

    solution_instance = Solution()
    print(solution_instance.romanToInt(s))
    print(s)


if __name__ == '__main__':
    main()

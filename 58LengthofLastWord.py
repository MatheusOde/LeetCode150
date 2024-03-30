class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for char in reversed(s):
            if char == ' ' and count > 0:
                break
            if char != ' ':
                count += 1
        return count


def main():
    s = "   fly me   to   the moon  "

    solution_instance = Solution()
    print(solution_instance.lengthOfLastWord(s))
    print(s)


if __name__ == '__main__':
    main()

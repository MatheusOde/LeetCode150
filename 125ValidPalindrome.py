import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.replace(" ", "").lower()

        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


def main():
    s = "A man, a plan, a canal: Panama"

    solution_instance = Solution()
    print(solution_instance.isPalindrome(s))
    print(s)


if __name__ == '__main__':
    main()

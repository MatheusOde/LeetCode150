class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        max_length = max(len(word) for word in strs)
        for i in range(max_length):
            for word in strs:
                print(i)
                if i < len(word):
                    print(word[i])


def main():
    strs = ["flower", "flow", "flight"]

    solution_instance = Solution()
    print(solution_instance.longestCommonPrefix(strs))
    print(strs)


if __name__ == '__main__':
    main()

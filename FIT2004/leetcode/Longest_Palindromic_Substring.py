class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        result = (0, 0)

        for index in range(len(s)):
            dp[index][index] = True
            result = (index, index)

        for end in range(len(s)):
            start = end

            while start >= 0:
                if s[start] == s[end]:
                    if (end - start == 1) or (end - start > 1 and dp[end - 1][start + 1]):
                        dp[end][start] = True

                        if end - start > result[1] - result[0]:
                            result = (start, end)

                start -= 1
        return s[result[0]:result[1] + 1]


if __name__ == "__main__":
    a = Solution()
    s = "babad"
    s = "cbbd"
    s = "acc"
    res = a.longestPalindrome(s)
    print(res)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        DP = [[ 0 for _ in range(len( word1 ) + 1) ] for _ in range(len(word2) + 1)]


        for i in range(len(word2)+1):
            DP[i][0] = i

        for i in range(len(word1)+1):
            DP[0][i] = i

        for i in range(1, len(word2) + 1):
            for j in range(1, len(word1) + 1):
                extra = 0
                if word1[j-1] != word2[i-1]:
                    extra = 1

                DP[i][j] = min(extra+ DP[i-1][j-1], 1 + DP[i-1][j], 1 + DP[i][j-1])

        self.print_matrix(DP)
        return DP[-1][-1]

    def print_matrix(self,M):
        for m in M:
            print(m)


if __name__ == "__main__":
    a = Solution()
    word1 = "intention"
    word2 = "execution"

    # word1 = "horse"
    # word2 = "ros"

    # word1 = "a"
    # word2 = ""
    res = a.minDistance(word1, word2)
    print(res)

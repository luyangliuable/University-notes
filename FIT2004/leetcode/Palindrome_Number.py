class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)

        i = 0
        while i != len( a )//2 + 1:
            print(a[i], a[-i], i)

            if a[i] != a[-i-1]:
                return False


            i += 1

        return True




if __name__ == "__main__":
    a = Solution()
    res = a.isPalindrome(10)
    print(res)

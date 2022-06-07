class Solution:
    def arraySign(self, nums: list[int]) -> int:
        res = 1
        # for num in nums:
        #     product = num*product
        for num in nums:
            if num < 0:
                res = -res

            if num == 0:
                return 0

        return res


if __name__ == "__main__":
    a = Solution()
    nums = [-1,-2,-3,-4,3,2,1]
    # nums = [1,5,0,2,-3]
    print(a.arraySign(nums))

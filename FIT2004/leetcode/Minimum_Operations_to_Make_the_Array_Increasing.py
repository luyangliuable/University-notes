class Solution:
    def minOperations(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return 0

        DP = [0]*len(nums)
        operations = 0

        DP[0] = nums[0]

        for i in range(len(nums)):
            if nums[i] <= DP[i]:
                operations += ( DP[i] - nums[i] )

            if i < len(nums)-1:
                DP[i+1] = max(nums[i+1], DP[i] + 1)

        return operations


if __name__ == "__main__":
    a = Solution()
    nums = [1,1,1]
    nums = [1,5,2,4,1]
    nums = [8]
    nums = []
    x = a.minOperations(nums)
    print(x)

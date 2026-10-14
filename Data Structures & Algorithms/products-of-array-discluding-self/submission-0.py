class Solution:
    def productExceptSelf(self, nums):

        n = len(nums)
        output = [1] * n

        # Left products
        left = 1

        for i in range(n):
            output[i] = left
            left = left * nums[i]

        # Right products
        right = 1

        for i in range(n - 1, -1, -1):
            output[i] = output[i] * right
            right = right * nums[i]

        return output
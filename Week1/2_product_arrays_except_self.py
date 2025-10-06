# https://leetcode.com/problems/product-of-array-except-self/description/

def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n

    # left products
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]

    # right products
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]

    return ans
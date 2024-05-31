"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i]
 is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""


def product_except_self_brute_force(nums):
    """
    Straight forward bruteforce algorithm for calculating product in O(n**2)

    :param nums:
    :return:
    """
    ans = []
    for i in range(0, len(nums)):
        temp = 1
        for j in range(0, len(nums)):
            if i != j:
                temp *= nums[j]
        ans.append(temp)
    return ans


def product_except_self_optimised(nums):
    """
    The idea is to precompute the prefix and suffix sum and then use those values as reference
    Time Complexity: 2 * O(N) = O(N)
    Space Complexity: O(3N)

    :param nums:
    :return:
    """
    prefix = [1]
    suffix = [1]
    tp = 1
    ts = 1
    ans = []
    for i in range(1, len(nums)):
        tp *= nums[i - 1]
        ts *= nums[len(nums) - i]
        prefix.append(tp)
        suffix.append(ts)
    # print(prefix)
    # print(suffix[::-1])
    for i, j in zip(prefix, suffix[::-1]):
        ans.append(i * j)
    return ans


def product_except_self_futher_optimised(nums):
    """
    Optimising the prefix and suffix product without additional space

    :param nums:
    :return:
    """

    ans = [1] * len(nums)
    curr = 1
    for i in range(0, len(nums)):
        ans[i] *= curr
        curr *= nums[i]
    curr = 1
    for i in range(len(nums) - 1, -1, -1):
        ans[i] *= curr
        curr *= nums[i]
    return ans


print(product_except_self_brute_force([1, 2, 3, 4]))
print(product_except_self_optimised([1, 2, 3, 4]))
print(product_except_self_futher_optimised([1, 2, 3, 4]))

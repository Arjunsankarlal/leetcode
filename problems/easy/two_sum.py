"""
https://leetcode.com/problems/two-sum/description/
"""


def two_sum(arr, target):
    """
    Bruteforce approach where it performs all the combinations in the worst case
    Time Complexity : O(n**2)
    Space Complexity : O(1)
    :param arr:
    :param target:
    :return:
    """
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]


def two_sum_dict(arr, target):
    """
    Quicker approach, where an additional space is taken up but runs faster
    Time Complexity : O(n)
    Space Complexity : O(n)
    :param arr:
    :param target:
    :return:
    """
    mapping = {}
    for i in range(0, len(arr)):
        if arr[i] in mapping:
            return [mapping[arr[i]], i]
        else:
            mapping[target - arr[i]] = i


nums = [2, 7, 11, 15]
target = 9
out = two_sum_dict(nums, target)
print(out)
out = two_sum(nums, target)
print(out)

nums = [3, 3]
target = 6
out = two_sum_dict(nums, target)
print(out)
out = two_sum(nums, target)
print(out)

nums = [3, 2, 4]
target = 6
out = two_sum_dict(nums, target)
print(out)
out = two_sum(nums, target)
print(out)

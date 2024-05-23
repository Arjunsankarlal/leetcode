"""
https://leetcode.com/problems/binary-search/description/
Given an array of integers nums which is sorted in ascending order,
 and an integer target, write a function to search target in nums.
  If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""


def binary_search(arr, st, en, target):
    if st > en:
        return -1
    mid = (st + en) // 2
    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binary_search(arr, st, mid, target)
    return binary_search(arr, mid, en, target)


nums = [-1, 0, 3, 5, 9, 12]

print(binary_search(nums, 0, len(nums) - 1, 9))

"""
https://leetcode.com/problems/merge-sorted-array/description/

First array length = len of first array + len of second array
This is a leetcode easy, but I would say it is medium hard
"""


def merge_arrays_with_additional_space(a, b):
    ans = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans.append(a[i])
            i += 1
        elif a[i] > b[j]:
            ans.append(b[j])
            j += 1
        else:
            ans.append(a[i])
            ans.append(b[j])
            i += 1
            j += 1
    while i < len(a):
        ans.append(a[i])
        i += 1

    while j < len(b):
        ans.append(b[j])
        j += 1
    return ans


def merge_arrays(a, b):
    """

    :param a:
    :param b:
    :return:
    """
    i = 0
    j = 0
    pass


# # Merge in-array with padded zeros
#
# a = [4, 5, 6, 0, 0, 0]
# b = [1, 2, 9]
#
# merge_arrays(a, b)
# print(a)
#
# a = [2, 3, 8, 0, 0, 0]
# b = [1, 7, 9]
# merge_arrays(a, b)
# print(a)
#
# a = [7, 8, 9, 0, 0, 0]
# b = [1, 2, 3]
# merge_arrays(a, b)
# print(a)

# Merge array with additional space
print(merge_arrays_with_additional_space([7, 8, 9], [1, 2, 3, 4]))
print(merge_arrays_with_additional_space([2, 4, 8], [1, 2, 3, 4]))

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


def merge_sort(nums):
    """
    Recursively splits the array into two until the split size becomes one,
    :param nums:
    :return:
    """
    if len(nums) == 1:
        return nums

    arr1 = nums[0:len(nums) // 2]
    arr2 = nums[len(nums) // 2:]

    split1 = merge_sort(arr1)
    split2 = merge_sort(arr2)

    return merge_arrays_with_additional_space(split1, split2)


print(merge_sort([5, 1, 3, 2, 9, 7, 6, 10, 8]))

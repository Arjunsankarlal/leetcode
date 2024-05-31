def insertion_sort(nums):
    """
    Array will be kept sorted at one end, while traversing the array we insert the new element to its
    corresponding position by swapping adjacent elements

    Time Complexity : O(n**2)
    Space Complexity : O(1)
    :param nums:
    :return:
    """
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    return nums


print(insertion_sort([5, 1, 3, 2, 9, 7, 6, 10]))

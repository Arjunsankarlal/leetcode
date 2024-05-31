def bubble_sort(nums):
    """
    Swapping adjacent elements according to the order till it is sorted

    Time Complexity : O(n**2)
    Space Complexity : O(1)
    :param nums:
    :return:
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(bubble_sort([4, 1, 6, 3, 2]))

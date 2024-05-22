def selection_sort(arr):
    """
    Shifting the most minimum elements one by one to start

    :param arr:
    :return:
    """
    for i in range(0, len(arr)):
        m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]
    return arr


print(selection_sort([5, 1, 3, 2, 9, 7, 6, 10]))

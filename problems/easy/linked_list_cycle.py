from problems.utils.ListNode import ListNode


def is_cycle_present(root):
    """
    Classic problem where one pointer travels 2x than the other pointer.
    so if there is a cycle the pointer will meet else list will end.

    :param root:
    :return:
    """
    if not root:
        return False
    if not root.next or not root.next.next:
        return False
    a = root.next
    b = root.next.next

    try:
        while a.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
    except Exception as e:
        return False


root = ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
# root.next.next.next.next = root.next.next

print(is_cycle_present(root))

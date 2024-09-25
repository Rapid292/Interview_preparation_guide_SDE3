class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a linked list in place.

    Examples:
        >>> linked_list = ListNode(1, ListNode(2, ListNode(3)))
        >>> reversed_list = reverse_linked_list(linked_list)
        >>> print(reversed_list.val)
        3
        >>> print(reversed_list.next.val)
        2
        >>> print(reversed_list.next.next.val)
        1
    """
    prev, curr = None, head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

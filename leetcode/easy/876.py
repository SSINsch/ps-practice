from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur_front, cur_double = head, head

        while cur_double.next:
            # forward one step
            cur_front = cur_front.next

            # forward two steps
            cur_double = cur_double.next
            if cur_double.next:
                cur_double = cur_double.next
            else:
                break

        return cur_front
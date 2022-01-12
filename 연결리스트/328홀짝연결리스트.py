# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

## 내 풀이..
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if odd == None:
            return None
        if head.next == None:
            return odd
        even = head.next
        node = head
        o_end = head
        e_end = head.next
        cnt = 1
        while node.next.next:
            next = node.next
            node.next = node.next.next
            if cnt % 2 == 1:
                o_end = node.next
            else:
                e_end = node.next
            node = next
            cnt += 1
        e_end.next = None
        
        o_end.next = even
        return odd
        
## 같은 방식이지만 좀더 정제된 코드

def oddEvenList(self, head : ListNode) -> ListNode:
    #예외처리
    if head is None:
        return None
    
    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    return head
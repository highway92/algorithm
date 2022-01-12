# Definition for singly-linked list.
# 반복문을 사용한 풀이
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(None)
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b
            head = head.next
            prev = prev.next.next
        return root.next
                
            

# 재귀적 구조를 이용한 풀이
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            p = head.next    
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
        
                
            
# Definition for singly-linked list.
# 내가 풀이한 코드..
# 리스트 -> 스트링 -> 또 리스트로 바뀐다. -> 문제는 없지만 코드 길이가 너무 길고 곧이 곧대로 풀이함
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []
        def reverse(head, array):
            if not head:
                return
            next = head.next
            array.append(str(head.val))
            return reverse(next, array)
        reverse(l1,list1), reverse(l2,list2)
        list1, list2 = list1[::-1],list2[::-1]
        result = str(int("".join(list1)) + int("".join(list2)))
        result = result[::-1]
        answer = []
        for i in result:
            answer.append(ListNode(int(i)))
        for i in range(len(answer)-1):
            answer[i].next = answer[i+1]
            
        return answer[0]


# 전가산기 아이디어를 이용한 코드

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = head = ListNode(0)
        
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            
            if l2:
                sum += l2.val
                l2 = l2.next
                
            carry,val = divmod(sum+carry, 10)
            head.next = ListNode(val)
            head = head.next
        return root.next
            
        
        
        
        
        
        
            
        
        
        
        
        
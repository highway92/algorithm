Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 테스트 케이스는 통과하였으나 실패한 코드.. 변수 설정이 직관적이지 못했다.
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = head
        cnt = 1
        node = head
        # 변수 설정
        while node:
            if left == 1:
                start = node
                S = node

            if cnt + 1 == left:
                start = node.next
                S = node
            
            if cnt + 1 == right:
                end = node.next
                E = node.next.next
                break
            node = node.next
            cnt += 1
        if left == 1:
            root = end
        # start 역순 노드 첫 번째 S는 start 바로 전 
        # end 역순 노드의 마지막 E는 end의 다음 노드
        r_node = start
        end.next = None
        prev = None
        while r_node:
            next = r_node.next
            r_node.next = prev
            prev = r_node
            r_node = next
        # 이제 S와 prev를 이어주고 start와 E를 이어주면 된다.
        S.next = prev
        start.next = E
        return root

        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def reverse(start_node, end_node):
    end_node.next = None
    node = start_node
    prev = None
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = next
    return



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev_start = ListNode(None)
        prev_start.next = head
        start = None
        end = None
        next_end = None
        prev_prev = None
        cnt = 1
        root = head
        node = head
        
        if not head or left == right:
            return head
        
        while node:
            next = node.next
            if cnt == left:
                start = node
                prev_prev = prev_start
                
            if cnt == right:
                end = node
                next_end = node.next
                break
                
            prev_start = prev_start.next
            node = next
            cnt += 1
        reverse(start,end)
        
        # if left == 1 and end.next == None:
        #     reverse(start,end)
        #     return end
        # 역순 연결 리스트의 (처음, 끝)
        if left == 1:
            root = end
            start.next = next_end
            return root
        # print(start,"\n",prev_prev,end,next_end)
        prev_prev.next = end
        start.next = next_end
        return root
            
            
        
        

        
        
            
            
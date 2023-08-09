# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    
    ### 문제풀이 1: 리스트를 활용
#         q: List = []
            
#         if not head:
#             return True
        
#         node = head
#         # 리스트 변환
#         while node is not None:
#             q.append(node.val)
#             node = node.next
            
#         # 팰린드롬 판별
#         while len(q) > 1:
#             if q.pop(0) != q.pop():
#                 return False
        
#         return True
        
    ### 문제풀이 2: 데크를 이용한 최적화
#         q: Deque = collections.deque()
            
#         if not head:
#             return True
        
#         node = head
#         # 리스트 변환
#         while node is not None:
#             q.append(node.val)
#             node = node.next
            
#         # 팰린드롬 판별
#         while len(q) > 1:
#             if q.popleft() != q.pop():
#                 return False
        
#         return True
    
    ### 문제풀이 3: 런너를 이용한 우아한 풀이 (rev: revised list, slow & fast runners)
        rev = None
        slow = fast = head
        #런너를 이용해 역순 연결리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
            
        #팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
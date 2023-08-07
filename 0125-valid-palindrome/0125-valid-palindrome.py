class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ### 문제 풀이 1
#         strs = []
            
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False

#         return True
        
        
        
        ### 문제풀이 2
        # 자료형 데크로 선언
#         strs: Deque = collections.deque()
            
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())

#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False

#         return True


        ### 문제풀이 3
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
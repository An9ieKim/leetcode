class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 확인
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True
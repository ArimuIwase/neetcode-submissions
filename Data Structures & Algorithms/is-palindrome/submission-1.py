class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned="".join([char for char in s if char.isalnum()]).lower()
        left=0
        right=-1
        for letters in range(len(cleaned)//2):
            if cleaned[left] != cleaned[right]:
                return False
            left+=1
            right-=1
        return True
        print (cleaned)
        
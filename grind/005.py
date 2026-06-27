class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        zero = ord("0")
        nine = ord("9")
        
        for char in s:
            small = char.lower()
            asc = ord(small)

            if asc >= 97 and asc <= 122 or asc>=zero and asc<=nine:
                # alpha numeric char
                arr.append(small)

        return True if arr == arr[::-1] else False
    


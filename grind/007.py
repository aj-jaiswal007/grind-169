class Solution:
    def get_hash(self, s: str)-> list[int]:
        arr = [0] * 26
        for char in s:
            arr[ord(char) - ord("a")]+=1
        
        return arr

    
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_hash(s) == self.get_hash(t)


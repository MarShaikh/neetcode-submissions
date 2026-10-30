class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two solutions:
        # first is reverse of string is equal to the string
        n_str = ""
        s = s.lower()
        for i in s:
            if i.isalnum():
                n_str += i
                
        return n_str == n_str[::-1]

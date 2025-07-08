class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_string = [i.lower() for i in s if i.isalnum()]
        print("".join(filtered_string))
        return "".join(filtered_string) == "".join(reversed(filtered_string))

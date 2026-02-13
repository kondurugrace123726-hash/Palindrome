"""
Problem: Palindrome Number

Given an integer x, return True if x is a palindrome,
and False otherwise.

A palindrome number reads the same backward as forward.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindrome
        if x < 0:
            return False
        
        # Convert number to string and compare with its reverse
        s = str(x)
        return s == s[::-1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))   # True
    print(solution.isPalindrome(-121))  # False
    print(solution.isPalindrome(10))    # False

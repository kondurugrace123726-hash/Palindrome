"""
Problem: Palindrome Number (Without String Conversion)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers or numbers ending in 0 (except 0 itself)
        # cannot be palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even digits: x == reversed_half
        # For odd digits: x == reversed_half // 10
        return x == reversed_half or x == reversed_half // 10
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False
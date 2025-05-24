# LeetCode Problem: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary to map Roman numerals to their integer values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0         # This will store the final integer result
        prev_value = 0    # Tracks the value of the previous Roman numeral

        # Iterate over the string in reverse (right to left)
        for char in reversed(s):
            value = roman[char]  # Get the integer value of the current Roman numeral

            # If the current value is less than the previous one, we subtract it
            # Example: IV -> 5 (V) comes before 1 (I), so we subtract 1 -> total = 4
            if value < prev_value:
                total -= value
            else:
                # Otherwise, we add it to the total
                total += value

            # Update prev_value to the current one for the next iteration
            prev_value = value

        return total  # Return the final converted integer

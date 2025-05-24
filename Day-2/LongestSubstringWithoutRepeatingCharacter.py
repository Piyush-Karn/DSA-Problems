# Problem: Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(str1):
    max_length = 0             # Tracks the maximum length found
    n = len(str1)              # Length of the input string

    # Loop through each character in the string as a starting point
    for i in range(n):
        sub1 = []              # Temporary list to store the current substring

        # Extend the substring one character at a time
        for j in range(i, n):
            if str1[j] not in sub1:
                sub1.append(str1[j])  # Add non-repeating character to the substring
            else:
                break                 # Stop when a repeating character is found

        # Update the max length if this substring is longer
        max_length = max(max_length, len(sub1))

    return max_length

# Example test cases
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")

def lengthOfLongestSubstring(str1):
    max_length = 0
    n = len(str1)

    for i in range(n):
        sub1 = []
        for j in range(i, n):
            if str1[j] not in sub1:
                sub1.append(str1[j])
            else:
                break
        max_length = max(max_length, len(sub1))  

    return max_length

print(lengthOfLongestSubstring("abcabcbb"))  
print(lengthOfLongestSubstring("bbbbb"))    
print(lengthOfLongestSubstring("pwwkew"))   

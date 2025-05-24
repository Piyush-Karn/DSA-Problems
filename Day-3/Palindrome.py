def isPalindrome(num):
    digit=0
    reversed=0
    while num!=0:
        digit = num%10
        reversed += digit*10
        num = num//10
        print(reversed)
    print(reversed)

isPalindrome(123)
    

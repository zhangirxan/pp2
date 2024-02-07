def isPalindrome(s):
    rev = ''.join(reversed(s))
 
    if (s == rev):
        print("Palindrome")
    else:
        print("Not palindrome")
 
s1=input()
print(isPalindrome(s1))
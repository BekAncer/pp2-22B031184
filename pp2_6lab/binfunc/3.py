def Palindrome(examp):
    t=examp[::-1]
    if examp != t:
        print("not palindrome")
    else:
        print('palindrome')
n=input()
Palindrome(n)
def is_Palindrome(num):
    org_num=num
    rev=0
    while num>0 :
        digit=num%10
        rev=rev*10+digit
        num=num // 10
    if rev==org_num :
        print(rev,"is a Palindrome number")
    else:
        print(rev, "is not a Palindrome number")
    
num=int(input('Enter a number:'))  
is_Palindrome(num)  
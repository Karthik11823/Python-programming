n=eval(input("Enter the number:"))
rev=0
original=n
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n//=10
if(original==rev):
    print("The given number is palindrome")
else:
    print("Not a palindrome")

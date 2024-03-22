n=int(input("Enter a number:"))
original=n
sum=0
while(n>0):
    a=n%10
    sum+=a*a*a
    n=n//10
if(sum==original):
    print("The number is amstrong")
else:
    print("Not a armstrong")

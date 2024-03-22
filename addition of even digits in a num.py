n=input("Enter a number:")
x=len(n)
n=int(n)
sum=0
for i in range(0,x,1):
    if((n%10)%2==0):
        sum+=n%10
    n//=10
print(sum)

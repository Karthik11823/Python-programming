n=eval(input("Enter a number:"))
sum=0
while(n>0):
    if((n%10)%2!=0):
        sum+=n%10
    n//=10
print(sum)

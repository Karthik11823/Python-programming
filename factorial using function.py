def fact(n):
    if(n==0 | n==1):
        return 1
    else:
        return n*fact(n-1)

n=eval(input("Enter a number:"))
f=fact(n)
print("Factorial of",n,"is",f)


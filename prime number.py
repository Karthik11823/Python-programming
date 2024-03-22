n=int(input("Enter a positive number:"))
for i in range(2,n):
    if(n%i==0):
        print("the number is not prime number")
        break
else:
    print("The number is prime number")

sum_even=0
sum_odd=0
n=int(input("Enter the number: "))
for i in range(1,n+1,1):
   if(i%2==0):
       sum_even+=i
   else:
       sum_odd+=i
print("sum of even = ",sum_even)
print("Sum of odd = ",sum_odd)

for n in range(1,1001,1):
   sum=0
   for i in range(1,n,1):
      if(n%i==0):
          sum+=i
   if(sum%n==0):
       print(n, "is perfect")

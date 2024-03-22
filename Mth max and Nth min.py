a=eval(input("Enter the list:"))
sort=sorted(a)
x=len(sort)
print(sort)
M=eval(input("Enter M value:"))
N=eval(input("Enter N value:"))
if(M<=x & N<=x):
    Mth_max=sort[-M]
    Nth_min=sort[N-1]
    sum=Mth_max + Nth_min
    difference=abs(Mth_max - Nth_min)
    print("Mth max number=",Mth_max)
    print("Nth min number=",Nth_min)
    print("sum=",sum)
    print("Difference=",difference)
else:
    print("Error:M and N are out of range")


    

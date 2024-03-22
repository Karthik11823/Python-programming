n=eval(input("Enter a number:"))
sp=0
sn=0
poscount=0
negcount=0
while(n!=-1):
    if(n>0):
        poscount+=1
        sp+=n
    else:
        negcount+=1
        sn+=n
    n=eval(input("Enter a number:"))
if (negcount>0):
    print("Average of negative is",sn/negcount)
else:
    print("No negative numbers were entered.")
if (poscount >0):
    print("Average of positive is",sp/poscount)
else:
    print("No positive numbers were entered.")

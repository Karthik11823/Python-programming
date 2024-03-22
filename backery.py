a=eval(input("Enter the number of fresh loaves purched:"))
b=eval(input("Enter the number of day old loaves purched:"))
regular_price=185.0
print("Regular price=",regular_price)

if a>=0:
    k=regular_price*a
    print("Amount of new loaves=",k)
    l=0
else:
    k=0
    print("Amount of new loaves=",k)
if b>=0:
    l=(regular_price*b*60)/100
    print("Amount of day old loaves=",l)
    k=0
else:
    l=0
    print("Amount of day old loaves=",l)
    
total=k+l
print("Total amount=",total)

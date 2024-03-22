def calculate_shipping_charge(num_items):
    if num_items<=0:
        return 0
    return 750+200*(num_items-1)

while True:
    a=eval(input("Enter the number of items purchased: "))
    num_items=a
    if(num_items>=0):
        break
    else:
        print("Number of items cannot be negative.")

shipping_charge=calculate_shipping_charge(num_items)
print("Shipping charge: {:.2f}".format(shipping_charge))


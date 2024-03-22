uppercount=0
lowercount=0
numbercount=0
while True:
    char=input("Enter the character:")
    if char=='*':
        break
    if char=='':
        break
    if char.isupper():
        uppercount+=1
    elif char.islower():
        lowercount+=1
    elif char.isdigit():
        numbercount+=1
print("Number of uppercase letters=",uppercount)
print("Number of lowercase letters=",lowercount)
print("Number count=",numbercount)
    

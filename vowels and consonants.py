a=input("Enter a string:")
vowels='aeiouAEIOU'
vowels_count=0
consonants_count=0
for char in a:
    if char.isalpha():
        if char in vowels:
            vowels_count+=1
        else:
            consonants_count+=1
print("Number of vowels=",vowels_count)
print("Number of consonants=",consonants_count)
 
 

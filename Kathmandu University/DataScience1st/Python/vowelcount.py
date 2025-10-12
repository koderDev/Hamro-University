text=input("Enter a string :")
v=0
c=0
vowels="aeiouAEIOU"
for char in text:
    if char in vowels:
        v+=1
    else:
        c+=1
print(f"The no. of vowels : {v}")
print(f"The no. of consonants : {c}")

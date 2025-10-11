text=input("Enter the string to reverse: ")
reverse=""
for i in range(len(text)-1,-1,-1):
    reverse+=text[i]
print(f"The reversed text is :{reverse}")

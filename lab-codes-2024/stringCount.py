s=input("Enter the string: ")
c=0
k=input("Enter the character: ")

for i in s:
    if(i==k):
      c=c+1
print("Number of occurences: ",c)
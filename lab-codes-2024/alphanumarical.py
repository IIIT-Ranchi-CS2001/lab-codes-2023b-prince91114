s=input("Enter the string: ")
c=0
for i in s:
    if(i.isalpha() or i.isalnum()):
        c=c+1
if c==len(s):
    print("True")
else:
    print("false")  

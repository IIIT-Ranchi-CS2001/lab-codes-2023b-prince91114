n=int(input("enter the number: "))
s=0

print("Number: ",n)
while(n>0):
    r=n%10
    s=s+r
    n=int(n/10)
print("sum of digits: ",s)
    

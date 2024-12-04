n=int(input("Enter the number of terms: "))
i=0

first=0
second=1
if(n==1):
    print("0",end=" ")
elif(n==2):
    print("0 1",end=" ")
 
else:
 while(n-2):
    if(i==0):
       print("0 1",end=" ")
       i=1
    sum=first+second
    print(sum,end=" ")
    first=second
    second=sum

    n=n-1
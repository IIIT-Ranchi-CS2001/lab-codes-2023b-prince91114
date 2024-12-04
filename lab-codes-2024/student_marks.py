Name=input("enter the name: ")
Roll_no=int(input("enter the roll number: "))
Marks=int(input("enter the marks: "))

if Marks>=90:
  Grade=10
  Remarks="OUTSTANDING"
elif Marks>=80:
  Grade=9
  Remarks="VERY GOOD"

elif Marks>=70:
  Grade=8
  Remarks="GOOD"

elif Marks>=60:
  Grade=7
  Remarks="AVERAGE"
  
elif Marks>=50:
  Grade=6
  Remarks="PASS"

elif Marks>=40:
  Grade=0
  Remarks="FAIL"

print(f"Name:{Name}")
print(f"Roll_no:{Roll_no}")
print(f"Marks:{Marks}")
print(f"Grade:{Grade}")
print(f"Remarks:{Remarks}")
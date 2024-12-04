import math
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

d= (b**2) - (4*a*c)

if d>=0:
  x=(-1*b + math.sqrt(d)) / (2*a)
  y=(-1*b - math.sqrt(d)) / (2*a)
  print(f"roots are {x} and {y}")


if d<=0:
  real_part=-b/(2*a)
  imaginary_part=math.sqrt(-d)/(2*a)
  print(f"imaginary part are{imaginary_part} and real part is{real_part}")
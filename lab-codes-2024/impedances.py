 
Z1_real = float(input("Enter the real part of Z1: "))
Z1_imag = float(input("Enter the imaginary part of Z1: "))
Z2_real = float(input("Enter the real part of Z2: "))
Z2_imag = float(input("Enter the imaginary part of Z2: "))

 
Z1 = complex(Z1_real, Z1_imag)
Z2 = complex(Z2_real, Z2_imag)

 
Z_eq = (Z1 * Z2) / (Z1 + Z2)

 
print("\nZ1 =", Z1)
print("Z2 =", Z2)
 
print("\nEquivalent impedance (Z_eq):", Z_eq)

 
print("\nReal part of Z_eq:", Z_eq.real)
print("Imaginary part of Z_eq:", Z_eq.imag)
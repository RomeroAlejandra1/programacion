num1=float(input("Ingrese el primer número:"))
num2=float(input("Ingrese el segundo número:"))
operación= input("seleccione la operación (+,-,*,/): ")

if operación =='+':
resultado=num1+num2
print(f"resultado:{resultado:.2f}")
elif operación =='-':
resultado=num1-num2
print(f"resultado:{resultado:.2f}")
elif operación =='*':
resultado=num1*num2
print(f"resultado:{resultado:.2f}")
elif operación =='/':
resultado=num1/num2
print(f"resultado:{resultado:.2f}")
if num2!=0:
resultado=num1/num2
print(f"resultado:{resultado:.2f}")
else:
print(f"ERROR ni se puede dividir entre 0")
else:
print(f"operación no valida")
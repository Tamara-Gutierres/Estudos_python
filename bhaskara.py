from math import sqrt

A = float(input("Informe A: "))
B = float(input("Informe B: "))
C = float(input("Informe C: "))

delta=B**2-4*A*C
if delta>=0:
    X1=(-B+sqrt(delta))/(2*A)
    X2=(-B-sqrt(delta))/(2*A)
    print("X1= "+str(X1)+"\nX2= "+str(X2))
else:
    print("impossivel calcular")
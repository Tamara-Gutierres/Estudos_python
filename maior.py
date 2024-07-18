A = int(input("Informe o A: "))
B = int(input("Informe o B: "))
C = int(input("Informe o C: "))

MaiorAB=(A+B+abs(A-B))/2

X=MaiorAB

o_maior=(X+C+abs(X-C))/2

print("o maior numero eh: "+str(o_maior))
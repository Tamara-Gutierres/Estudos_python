N=int(input("Informe o tamanho da matriz: "))
Matriz=[]
for i in range (0,N):
    Linha=[] 
    for j in range (0,N):
        Elementos=int(input("informe os elementos da matriz: "))
        Linha.append(Elementos)
    Matriz.append(Linha)

print(Matriz)
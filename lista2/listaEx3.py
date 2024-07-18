Matriz1=[[1,2],
         [3,4]]
Matriz2=[[5,6],
         [7,8]]
#soma
soma=[]
for i in range (0,2):
    GuaradarParaSoma=[] #linha
    for j in range (0,2):
        GuaradarParaSoma.append(Matriz1[i][j]+Matriz2[i][j])
    soma.append(GuaradarParaSoma)
#print(soma)

#Matriz1 x Matriz2
MatrizFinal=[]
for i in range(0,2):
    Linha=[]
    for j in range (0,2):
        Linha.append((Matriz1[i][j]*Matriz2[j][j])+(Matriz1[i][i]*Matriz2[i][j]))
    MatrizFinal.append(Linha)
print(MatrizFinal)
# terminar essa3 nm
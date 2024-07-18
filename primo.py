quantidade_de_numeros=int(input("informe a quantidade de numeros:"))
numeros = []
for i in range (0,quantidade_de_numeros):
    numeros.append(int(input("digite o numero: "))) #append ele guarda o valor no final da lista
for n in numeros: #n é um numero da lista numeros
    for dividendo in range (2,n):
        x=n % dividendo
        if x==0:
            print ("Not prime "+ str(n))
            break #para o for dividendo
        if n-1==dividendo: #n-1, pois no range ele nunca chega no n
            print ("Prime "+ str(n))
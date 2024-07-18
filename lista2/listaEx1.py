'''Nome1=input("digite o primeiro nome: ")
Nome2=input("digite o segundo nome: ")
Nome3=input("digite o terceiro nome: ")
Nome4=input("digite o quarto nome: ")

Idade1=int(input("Digite a primeira idade: "))
Idade2=int(input("Digite a segunda idade: "))
Idade3=int(input("Digite a terceira idade: "))
Idade4=int(input("Digite a quarta idade: "))

nomes_idades={Nome1 : Idade1,
              Nome2 : Idade2,
              Nome3 : Idade3,
              Nome4 : Idade4}
print(nomes_idades)


nomes_idades['gabriel'] = 21 

print(nomes_idades)'''

nomes_idades={}
for i in range(0,3):
    Nomes=input("digite o nome")
    Idades=int(input("digite a idade"))
    nomes_idades[Nomes]=Idades
print(nomes_idades)

    
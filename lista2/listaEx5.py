arquivo = open ("nomes.txt", 'r')
Lista=[]
for nome in arquivo:
    Lista.append(nome)
print('A quantidade de Gabriel é: ' +str(Lista.count('Gabriel\n')))
print('A quantidade de Herique é: ' +str(Lista.count('Henrique\n')))
print('A quantidade de Laura é: ' +str(Lista.count('Laura\n')))
arquivo.close()

#escrevndo em outro arquivo
arquivo = open ("nomesinvertido.txt", 'w')
for nome in Lista:
    arquivo.write(nome)
arquivo.close()

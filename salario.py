NumeroDoFuncionario= int(input("Informe o seu numero: "))
HorasTrabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
ValorPorHorasTrabalhadas= float(input("Informe o valor por horas trabalhadas: "))

salario=HorasTrabalhadas*ValorPorHorasTrabalhadas
print('Numero do funcionario: '+str(NumeroDoFuncionario)+
      "\nSalario: "+str(salario))

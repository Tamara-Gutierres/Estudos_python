ano=int(input("informe o ano: "))
if ano>=2000:
    comum = True
    huluculu=ano%15
    if huluculu==0:
        print ("huluculu")
        comum = False

    bissexto1=ano%4
    bissexto2=ano%100
    bissexto3=ano%400
    if bissexto1==0 and bissexto2!=0:
        print ("ano bissexto")
        comum = False

    if bissexto2==0 and bissexto3==0:
        print ("ano bissexto")
        comum = False
        
        bulukulu=ano%55
        if bulukulu==0:
            print("bulukulu")
            
    if comum:
        print("Ano comum")

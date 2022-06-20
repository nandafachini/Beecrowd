#1125 - Professor, mas é só 0,5

trabalho = float(input())
prova = float(input())

media = (trabalho + prova) * 0.5

if media <6:
    if media >=1:
        if trabalho >=2:
            print("talvez com a sub")
        else:
            print("reprovado")
    else:
        print("reprovado")
else:
    print("aprovado")

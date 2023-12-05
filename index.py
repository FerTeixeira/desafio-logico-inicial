while True:
    nome = str(input("Nome do Herói: "))
    xp = int(input(f"Quanto de XP o Herói {nome} possui: "))
    if xp <= 1000:
        print(f"O Herói {nome} é Ferro")

    elif xp >= 1001 and xp <=2000:
        print(f"O Herói {nome} é Bonze")

    elif xp >= 2001 and xp <=5000:
        print(f"O Herói {nome} é Prata")

    elif xp >= 5001 and xp <=6000:
        print(f"O Herói {nome} é Ouro")

    elif xp >= 6001 and xp <=7000:
        print(f"O Herói {nome} é Platina")

    elif xp >= 7001 and xp <=8000:
        print(f"O Herói {nome} é Diamante")

    elif xp >= 8001 and xp <=9000:
        print(f"O Herói {nome} é Ascendente")

    elif xp >= 9001 and xp <=10000:
        print(f"O Herói {nome} é Imortal")

    else:
        print(f"O Herói {nome} é Radiante")

    r = str(input("Deseja consultar outro Herói(N/n para sair)? "))
    if r == 'N' or r =='n':
        break
    else:
        continue
    



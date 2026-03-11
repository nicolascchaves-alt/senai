soma = 0 
acima_15 = 0
acima_20 = 0
sobrecarga = False
alerta = False
acima_200 = 0
for cont in range(8):
    amper = float(input(f"digite o {cont + 1} amper: "))
    soma += amper
    if amper > 15:
        acima_15 += 1
    if amper > 20:
        sobrecarga = True
        acima_20 += 1
        if amper + 200:
            alerta = True
            acima_200 += 1 

media = soma / 8
print(f"Amper media: {media}") 
print(f"quantidade de amperes acima de 15: {acima_15} vezes")
if sobrecarga:
    print(" houve sobrecarga no motor {acima_20} vezes")
if alerta:
    print("alerta: ultrapassou 200 {acima_200} vezes")
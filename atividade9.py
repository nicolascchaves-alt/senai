soma = float()
maior = float()
menor = float()
acima_100 = 0

for i in range(10):
    temp = float(input(f"Temperatura {i+1}: "))
    soma += temp
    
    if i == 0:
        maior = temp
        menor = temp
    else:
        if temp > maior:
            maior = temp
        if temp < menor:
            menor = temp
    
    if temp > 100:
        acima_100 += 1

media = soma / 10

print(f"\nMaior temperatura: {maior}°C")
print(f"Menor temperatura: {menor}°C")
print(f"Média das temperaturas: {media:.2f}°C")
print(f"Vezes que ultrapassou 100°C: {acima_100}")

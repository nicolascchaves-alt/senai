peso = float(input("Digite o peso da pessoa (em kg): "))

peso_engordado = peso + (peso * 0.15)

peso_emagrecido = peso - (peso * 0.20)

print(f"Peso original: {peso:.2f} kg")
print(f"a) Peso se engordar 15%: {peso_engordado:.2f} kg")
print(f"b) Peso se emagrecer 20%: {peso_emagrecido:.2f} kg")

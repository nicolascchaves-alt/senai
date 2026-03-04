nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade:"))
while idade > 120 or idade < 0:
    idade = int(input)("idade(anos completos - ate 120)")
dias_vida = idade * 365
print(f"{nome}, voce viveu {dias_vida}")

    


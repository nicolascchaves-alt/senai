medicoes
 
 print("digite 8 medicoes de corrente elétrica (em amperes):")
for i in range(8):
    corrente = float(input(f"Medicao {i+1}: "))
    medicoes.append(corrente)

acima_15a = sum(1 for m in medicoes if m > 15)
sobrecarga = any(m > 20 for m in medicoes)

media_corrente = sum(medicoes) / len(medicoes)
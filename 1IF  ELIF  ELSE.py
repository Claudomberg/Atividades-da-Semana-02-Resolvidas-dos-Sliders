i = int(input("Digite a idade: "))
r = float(input("Digite a renda: "))

if r >= 10000 and i >= 18:
    _ = "Diamante"
elif r >= 5000:
    _ = "Ouro"
elif r >= 2000:
    _ = "Prata"
else:
    _ = "Bronze"

print(f"Classificação: {_}")
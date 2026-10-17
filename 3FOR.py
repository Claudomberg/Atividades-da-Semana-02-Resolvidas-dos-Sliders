n = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    n.append(num)

soma = sum(n)
media = soma / 5
maior = max(n)
menor = min(n)

print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
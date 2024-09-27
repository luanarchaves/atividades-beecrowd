
age = int(input())
data = [365, 30, 1]
contagem = [0, 0, 0]
i = 0

while age > 0:
    if (age >= data[i]):
        contagem[i] += 1
        age -= data[i]
    else:
        i += 1

print(f'{contagem[0]} ano(s)')
print(f'{contagem[1]} mes(es)')
print(f'{contagem[2]} dia(s)')


notas = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

notas_add = [0] * 6
moedas_add = [0] * 6

valor = float(input())

i = 0
while i < 6:
    if (valor > notas[i]):
        valor -= notas[i]
        notas_add[i] += 1
    else:
        i += 1

j = 0
while j < 6:
    if (valor > moedas[j]):
        valor -= moedas[j]
        moedas_add[j] += 1
    else:
        j += 1

print('NOTAS:')
for i in range(6):
    print(f'{notas_add[i]} nota(s) de R$ {str(f"{notas[i]:.2f}")}')

print('MOEDAS:')
for i in range(6):
    print(f'{moedas_add[i]} moeda(s) de R$ {str(f"{moedas[i]:.2f}")}')
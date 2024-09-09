
numeros = ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00']
value = [100, 50, 20, 10, 5, 2, 1]
notas = [0, 0, 0, 0, 0, 0, 0]

numb = int(input())
print(numb)

i = 0

for i in range(7):
    if numb >= int(value[i]):
        while numb >= int(value[i]):
            numb -= int(value[i])
            notas[i] += 1


for i in range(7):
    print(f'{notas[i]} nota(s) de R$ {numeros[i]}')
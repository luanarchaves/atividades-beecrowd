nome = input()
salariFixo = float(input())
vendas = float(input())

total = salariFixo + (0.15 * vendas)

print(f'TOTAL = R$ {total:.2f}')
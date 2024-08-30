peça1 = input()
peça2 = input()

valor1 = peça1.split()
valor2 = peça2.split()

soma = float(valor1[1]) * float(valor1[2]) + float(valor2[1]) * float(valor2[2]) 


print(f'VALOR A PAGAR: R$ {soma:.2f}')
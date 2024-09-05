a,b,c = list(map(float,input().split()))

'''
py le os comandos do mais interno para o mais externo, primeiro ele le o 'input'
e depois o 'slipt', pq o input retorna uma string e slipt é um metodo de string (trasformar em listra)
depois é executado 'map(float, )' o map aplica uma função a cada elemento da listra, nesse caso é a 
conversão das string para um float, porém ele não trasforma em uma listra e sim em uma interavel 
(objeto em Python que pode ser percorrido, ou seja, pode ser "iterado" elemento por elemento.),
depois o resultado disso é a conversão para uma listra.
'''

pi = 3.14159

areaTrianglo = (a * c) / 2

areaCirculo = pi * (c**2)
areaTrapezio = ((a+b) * c) / 2
areaQuadrado = b**2
areaRetangulo = a*b

print(f'TRIANGULO: {areaTrianglo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')


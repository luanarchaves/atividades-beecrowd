a,b,c = list(map(int, input().split()))

MaiorAB = int((a + b + abs(a-b)) / 2)

if a > MaiorAB:
    print(f'{a} eh o maior')
elif b > MaiorAB:
    print(f'{b} eh o maior')  
elif c > MaiorAB:
    print(f'{c} eh o maior')  
else:
    print(f'{MaiorAB} eh o maior')  







    


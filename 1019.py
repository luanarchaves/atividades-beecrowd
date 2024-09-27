value = int(input())

hora = int(value // 3600) 
minuto = int(value - (hora*3600))
segundo = int(minuto - ((minuto//60)*60))

minuto = int(minuto // 60)

print(f'{hora}:{minuto}:{segundo}') 
with open("./advent-of-code-2022/Day 1/input.txt", "r") as f:
    lineas = f.readlines()
    lineas = [linea[:-1] for linea in lineas]

caloriasPorElfo = []
caloriasTemp = 0
for linea in lineas:
    if linea == "":
        caloriasPorElfo.append(caloriasTemp)
        caloriasTemp = 0 
        continue

    caloriasTemp += int(linea)
caloriasPorElfo.append(caloriasTemp) # Agrega el ultimo valor

del caloriasTemp

res = 0
for i in range(3):
    res += max(caloriasPorElfo)
    maxIndex = caloriasPorElfo.index(max(caloriasPorElfo))
    caloriasPorElfo.pop(maxIndex)
    
print(res)
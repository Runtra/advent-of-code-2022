with open("./advent-of-code-2022/Day 1/input.txt", "r") as f:
    lineas = f.readlines()
    lineas = [linea[:-1] for linea in lineas]


caloriasMaximas = 0
caloriasElfo   = 0
for linea in lineas:
    if linea == "":
        if caloriasElfo >= caloriasMaximas:
            caloriasMaximas = caloriasElfo
        caloriasElfo = 0
        continue
    caloriasElfo += int(linea)

print(caloriasMaximas)
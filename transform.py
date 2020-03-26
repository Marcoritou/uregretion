import csv

def aprox(N):
    out = '%s' % float('%.3g' % N)
    return(out)

with open('newdata.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

nuevosdatos = []
longitud = len(data)
longitud2 = len(data[0])

for i in range(longitud):
    nuevosdatos.append([0] * longitud2)

for j in range(longitud2):
    K = data[0][j]
    nuevosdatos[0][j] = K
    
for i in range(1,longitud):
    for j in range(longitud2):
        N = data[i][j]
        N = float(N)
        N = aprox(N)
        nuevosdatos[i][j] = N
        
for i in range(longitud):
    for j in range(longitud2):
        if j != longitud2-1:
            print(nuevosdatos[i][j],end=",")
        if j == longitud2-1:
            print(nuevosdatos[i][j],end="")
    print(end="\n")






        

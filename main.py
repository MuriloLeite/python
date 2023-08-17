lista = []
lista_pares = []
for i in range(1001):
     lista.append(i)
for j in range(len(lista)):
    if j % 2 == 0:
        lista_pares.append(j)


print(lista)
print(".........")
print(lista_pares)
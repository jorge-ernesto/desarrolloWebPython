#Manejo de listas

#Creacion de lista
lista_elementos = [23,2,3,'Cadena texto','3',34.34]

#Anexar un nuevo elemento
lista_elementos.append('Nueva cadena de texto')

print('Uso de la sentencia for')
for elemento in lista_elementos:
    print(elemento)

#Anexar un nuevo elemento
lista_elementos.append(35)
print('Recorrido de la lista con while')
longitud_lista = len(lista_elementos)
counter = 0
while counter < longitud_lista:
    print(lista_elementos[counter])
    counter = counter + 1

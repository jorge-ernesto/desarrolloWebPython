import datetime

def nombreFuncion(parametro_funcion):
    print('Hola bienvenido a esta funcion')
    print(parametro_funcion)

def numCuadrado(num_x):
    num_final = num_x*num_x
    return num_final

nombre = 'Alexander'
num_prueba = 25
nombreFuncion(nombre)
resultado_prueba = numCuadrado(num_prueba)
print(resultado_prueba)

print(datetime.datetime.now())
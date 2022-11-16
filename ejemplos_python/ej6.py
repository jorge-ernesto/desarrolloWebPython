class estudiante:
    def __init__(self):
        nombre = ''
        apellido = ''
        edad = ''
        codigo = ''
        cicloEstudios = ''
        universidadEstudiante = ''
    def imprimir(self):
        print('Hola a todos desde la clase estudiante')

est_1 = estudiante()
est_1.nombre = 'Javier'
est_1.apellido = 'Hilario'
est_2 = estudiante()
est_2.nombre = 'Alexander'
est_2.apellido = 'Segovia'

est_1.imprimir()

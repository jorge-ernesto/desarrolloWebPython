import numpy
import time

a = numpy.random.rand(1000000)
b = numpy.random.rand(1000000)


tic = time.time()
c = numpy.dot(a,b)
toc = time.time()

print('El tiempo de multiplicacion con numpy es : ' + str(1000*(toc-tic)) + ' ms')

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()

print('El tiempo de ejecucion en un bucle es de ' + str(1000*(toc-tic)) + ' ms')

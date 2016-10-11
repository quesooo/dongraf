import timeQ
from random import randint

print timeQ.monotonic_time()

tInicial=timeQ.monotonic_time()
i=0
while i < 1000000: #Contar desde 0 a 10e10
	i+=1
print "tiempo en contar 10e6"
print timeQ.monotonic_time()-tInicial
import numpy
import time

filepath = './data_test_1k'
price = numpy.random.normal(1000, 150, 1000)
qty = numpy.random.normal(3, 2, 1000)
time = numpy.random.normal(1502289181, 100000, 1000)
f = open(filepath, 'w')
for i in range(1000):
    hq = numpy.random.rand() > .8
    if hq:
        seller = "Moneybags"
    else:
        seller = "Commoner"
    if int(qty[i]) <= 0:
        qty[i] = 1

    entry = ('Sword', time[i], hq, int(price[i]), seller, int(qty[i]))
    print entry
    f.write(str(entry))
    f.write('\n')
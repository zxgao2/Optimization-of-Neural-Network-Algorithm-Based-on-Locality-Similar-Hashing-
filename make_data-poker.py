# -*- coding: utf-8 -*-
import libpylshbox as pylshbox
import numpy as np
import time
from sklearn import datasets
import os
import cPickle
import numpy
from PIL import Image
import commondata

dirname = 'pokert'
myfile = 'test-poker.pkl'

number = 1000000


pictures = numpy.empty((number,10))
lables = numpy.empty(number)

index = 0
lable = 0
index1 = 0
number1 = 0
Data_begin = []
Data_end = []
file = open("poker")

while 1:
    line = file.readline()
    if not line:
       break
    a = []
    line1 = line.split(' ')
    for i in range(1,11):
        line2 =line1[i].split(':')
        a.append(int(line2[1]))
    image_narray = numpy.asarray(a,dtype = 'float64')/20
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])
    index= index+1



lables = lables.astype(numpy.int)
write_file=open(myfile,'wb')
cPickle.dump([pictures[:],lables[:],commondata.Data_begin_end[:],commondata.Data_index[:]],write_file,-1)
write_file.close()

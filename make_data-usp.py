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

dirname = 'usps.t'
myfile = 'test-usps.pkl'

number = 2007


pictures = numpy.empty((number,256))
lables = numpy.empty(number)

index = 0
lable = 0
index1 = 0
number1 = 0
Data_begin = []
Data_end = []
file = open(dirname)

while 1:
    line = file.readline()
    if not line:
       break
    a = []
    line1 = line.split(' ')
    for i in range(1,257):
        line2 =line1[i].split(':')
        a.append(float(line2[1]))
    image_narray = numpy.asarray(a,dtype = 'float64')
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])-1
    index= index+1



lables = lables.astype(numpy.int)
write_file=open(myfile,'wb')
cPickle.dump([pictures[:],lables[:],commondata.Data_begin_end[:],commondata.Data_index[:]],write_file,-1)
write_file.close()

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
import math

dirname = 'satimage.scale.txt'
myfile = 'train-sat.pkl'

number = 4435

pictures = numpy.empty((number,36))
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
    k=1;
    for i in range(1,37):
        # print line1[i]
        #  print k
        if k<len(line1):
            line2 =line1[k].split(':')
        if int(line2[0]) == i :
            a.append(float(line2[1]))
            k=k+1
        else:
            a.append(0)
    # print  a

    image_narray = numpy.asarray(a,dtype = 'float64')
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])-1
    index= index+1

f=open("sat.txt","w+")

print len(pictures)
for i in pictures:
    for j in range(len(i)):
        f.write(str(i[j])+'\t')
    f.write('\n')

f.close()

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

dirname = 'pendigits.txt'
myfile = 'train-pen.pkl'

number = 7494

pictures = numpy.empty((number,16))
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
    for i in range(1,17):
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

    image_narray = numpy.asarray(a,dtype = 'float64')/100
    pictures[index] = numpy.ndarray.flatten(image_narray)
    lables[index] = int(line1[0])
    index= index+1

f=open("pen.txt","w+")

print len(pictures)
for i in pictures:
    for j in range(len(i)):
        f.write(str(i[j])+'\t')
    f.write('\n')

f.close()

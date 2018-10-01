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
import random
import math
dirname = 'test'
myfile = 'train2.pkl'

number = 0
for filename in os.listdir(dirname):
 if filename == '.DS_Store' or filename == '0' or filename == '6' or filename == '7' or filename == '8' or filename == '9' or filename == '4' or filename == '2' or filename == '1' or filename == '3'  :
  continue
 else:
    filename1 = dirname + '/' + filename
    for filename2 in os.listdir(filename1):
        if filename2 == '.DS_Store':
         continue
        else:
         number += 1

pictures = numpy.empty((number,commondata.ImageWidth*commondata.ImageHeight))
lables = numpy.empty(number)

index = 0
lable = 0
index1 = 0
number1 = 0
Data_begin = []
Data_end = []
k = 200
for filename in os.listdir(dirname):
 if filename == '.DS_Store' or filename == '0' or filename == '6' or filename == '7' or filename == '8' or filename == '9' or filename == '1' or filename == '2' or filename == '4' or filename == '3'  :
  continue
 else:
    filename1 = dirname + '/' + filename
    for filename2 in os.listdir(filename1):
        if filename2 == '.DS_Store' :
            continue
        else:
           filename2 = filename1 + '/' + filename2
           image = Image.open(filename2)
           image = image.convert('L')
           image = image.resize((commondata.ImageHeight,commondata.ImageWidth))
           image_narray = numpy.asarray(image,dtype = 'float64')/256
           pictures[index] = numpy.ndarray.flatten(image_narray)
           lables[index] = lable
           index = index + 1
           number1 += 1

    lable= lable +1
    number1 = 0



f=file("mnist.txt","w+")

print len(pictures)
for i in pictures:
    for j in range(len(i)):
        f.write(str(i[j])+'\t')
    f.write('\n')

f.close()





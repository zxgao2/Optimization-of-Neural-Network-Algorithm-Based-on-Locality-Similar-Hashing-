# -*- coding: utf-8 -*-

import numpy
import commondata
from PIL import Image
import cPickle
import myalgorithm

filename = 'test1.jpg'

read_file = open('weight.pkl','rb')
weights,biases = cPickle.load(read_file)
read_file.close()

def outcome(weights,biases,a):
    for b,w in zip(biases,weights):
        a = myalgorithm.sigmoid(numpy.dot(w,a)+b)
    return numpy.argmax(a)

def get_predict(filename):
    image = Image.open(filename)
    image = image.convert('L')
    image = image.resize((commondata.ImageHeight,commondata.ImageWidth))
    image_narray = numpy.asarray(image,dtype = 'float64')/256
    image_vector = numpy.ndarray.flatten(image_narray)
    test = numpy.reshape(image_vector,(commondata.ImageHeight*commondata.ImageHeight,1))
    result = outcome(weights,biases,test)
    print result

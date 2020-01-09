import numpy as np
import matplotlib.pyplot as plt
import os
import time
import imageio
import math
from numpy.random import randn
from numpy.random import randint


data_dir = 'datasets/img_align_celeba'
images = os.listdir(data_dir)
attribute_dir = 'datasets/list_attr_celeba.txt'
attrs = []
with open(attribute_dir) as f:
  attrs = f.readlines()

#get the image count
img_count = int(attrs[0])

#get attrs for each image
image_attrs = attrs[2:]

#separate images according to hair color, in this dataset
#we have Black_Hair Blond_Hair and BrownHair, respectively in index 
#9,10,12
black_hair_file_names = []
blonde_hair_file_names = []
brown_hair_file_names = []

for i in range(img_count):
    #first split into different attrs
    img_attr = image_attrs[i].split(' ')
    #filter empty string
    img_attr = [x for x in img_attr if x != '' ]
    
    #then extract hair feature
    black = img_attr[9]
    blonde = img_attr[10]
    brown = img_attr[12]
    
    #then append file names according to hair color
    if black == '1':
        black_hair_file_names.append(img_attr[0])
    elif blonde == '1':
        blonde_hair_file_names.append(img_attr[0])
    elif brown == '1':
        brown_hair_file_names.append(img_attr[0])

output_path = 'datasets/img_align_celeba'

#divide each dataaset into training set and testing set
rate = .75
black_count = len(black_hair_file_names)
black_count_t = math.floor(black_count * rate)
blonde_count = len(blonde_hair_file_names)
blonde_count_t = math.floor(blonde_count * rate)
brown_count = len(brown_hair_file_names)
brown_count_t = math.floor(brown_count * rate)
c = 0
#start to read images
for i in range(len(black_hair_file_names)):
    img = plt.imread(data_dir + '/' + black_hair_file_names[i])
    if c <= black_count_t:
        plt.imsave(output_path+'/'+'trainA/'+'{}'.format(black_hair_file_names[i]),img)
        c+=1
        print("a black finsih")
        #os.remove(data_dir + '/' + black_hair_file_names[i])
    else:
        plt.imsave(output_path+'/'+'testA/'+'{}'.format(black_hair_file_names[i]),img)
        #os.remove(data_dir + '/' + black_hair_file_names[i])

c = 0

for i in range(len(blonde_hair_file_names)):
    img = plt.imread(data_dir + '/' + blonde_hair_file_names[i])
    if c <= blonde_count_t:
        plt.imsave(output_path+'/'+'trainB/'+'{}'.format(blonde_hair_file_names[i]),img)
        c+=1
        print("a blonde finsih")
        #os.remove(data_dir + '/' + blonde_hair_file_names[i])
    else:
        plt.imsave(output_path+'/'+'testB/'+'{}'.format(blonde_hair_file_names[i]),img)
        #os.remove(data_dir + '/' + blonde_hair_file_names[i])




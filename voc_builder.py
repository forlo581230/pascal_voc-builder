# -*- coding: utf-8 -*-
from glob import glob
import os
import numpy as np
import shutil

DATASET_NAME = 'VOC2017'

path = './data'
folder_paths = glob(os.path.join(path, '*'))
os.mkdir(os.path.join(path,'test'))
os.mkdir(os.path.join(path,'train'))
os.mkdir(os.path.join(DATASET_NAME))
os.mkdir(os.path.join(DATASET_NAME,'ImageSets'))
os.mkdir(os.path.join(DATASET_NAME,'ImageSets','Main'))
os.mkdir(os.path.join(DATASET_NAME,'Annotations'))
os.mkdir(os.path.join(DATASET_NAME,'JPEGImages'))

#makeing txt
ftrain = open(DATASET_NAME+'/ImageSets/Main/train.txt', 'w')
ftest = open(DATASET_NAME+'/ImageSets/Main/test.txt', 'w')

for folder_path in folder_paths:
    files = glob(os.path.join(folder_path,'*.jpg'))
    print ('Total no of images ',len(files))
    no_of_images = len(files)
    #train_images = (int)(no_of_images*0.2)
    train_images = 750
    shuffle = np.random.permutation(no_of_images)

    for t in ['train','test']:
        os.mkdir(os.path.join(path,t,folder_path.split('/')[-1]))
        
    #making train dataset
    for i in shuffle[:train_images]:
        #copying img to $path/train
        folder = files[i].split('/')[-2]
        image = files[i].split('/')[-1]
        shutil.copyfile(files[i],os.path.join(path,'train',folder,image))
        #copying xml to $path/train
        xml_path = files[i].split('.')[0]+'.xml'
        folder = xml_path.split('/')[-2]
        xml = xml_path.split('/')[-1]
        shutil.copyfile(xml_path,os.path.join(path,'train',folder,xml))
        #
        shutil.copyfile(files[i],os.path.join('VOC2017','JPEGImages',image))
        shutil.copyfile(xml_path,os.path.join('VOC2017','Annotations',xml))
        ftrain.write(image.split('.')[0]+'\n')
        
    #making test dataset
    for i in shuffle[train_images:]:
        #
        folder = files[i].split('/')[-2]
        image = files[i].split('/')[-1]
        shutil.copyfile(files[i],os.path.join(path,'test',folder,image))
        #
        xml_path = files[i].split('.')[0]+'.xml'
        folder = xml_path.split('/')[-2]
        xml = xml_path.split('/')[-1]
        shutil.copyfile(xml_path,os.path.join(path,'test',folder,xml))
        #
        shutil.copyfile(files[i],os.path.join('VOC2017','JPEGImages',image))
        shutil.copyfile(xml_path,os.path.join('VOC2017','Annotations',xml))
        ftest.write(image.split('.')[0]+'\n')
    
       
ftrain.close()   
ftest.close()   

#im_names =[];
#with open('VOC2017/ImageSets/Main/test.txt') as fp:
#    for line in fp:
#        im_names.append(line.strip('\n')+'.jpg')
        


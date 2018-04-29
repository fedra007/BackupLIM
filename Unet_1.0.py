__author__= "fedra_trujillano"
# Basado en https://www.kaggle.com/drn01z3/end-to-end-baseline-with-u-net-keras

#import numpy as np
#import cv2
import pandas as pd
#import tifffile as tiff
#import random

#Numero de clases 0: Blured 1: Corn1 2:Corn2 3:Corn3 4:Corn4 5:Unknown 6:Potato 7:River 8:Road 9:Building 
Num_Clases = 10

#Path to the images and masks
imDir='/home/fedra/Documents/SANT_test'
filesDir='/home/fedra/Documents/SANT_test'

#size of the patches (square)

def joinMasks(file):
	with open(file, "r") as openFile:
		for line in openFile:
			if (line[0]!='#'):
				print line  
	return

if __name__ =='__main__':
	joinMasks(filesDir+'/huapra060318_e1_mask.txt')


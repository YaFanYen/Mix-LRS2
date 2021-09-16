# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:48:02 2019

@author: Milk
"""
import os
import glob
import os.path
import numpy as np
import soundfile as sf

ch1path = '/home/ed716/Documents/NewSSD/Cocktail/lrs2_spk4_ch1'
ch2path = '/home/ed716/Documents/NewSSD/Cocktail/lrs2_spk4_ch2'
savepath = '/home/ed716/Documents/NewSSD/Cocktail/lrs2_spk4/'

ch1 = glob.glob(os.path.join(ch1path, '*', '*', '*.wav'))
ch2 = glob.glob(os.path.join(ch2path, '*', '*', '*.wav'))

for i in ch1:
    for j in ch2:
        if i.split('/')[-1] == j.split('/')[-1]:
            channel1, fs = sf.read(i, always_2d=True)
            channel2, fs = sf.read(j, always_2d=True)
            mixchannel = np.concatenate((channel1, channel2), axis=1)
            
            name = i.split('/')[-1]
            path = savepath + i.split('/')[-3] + '/' + i.split('/')[-2]
            if not os.path.isdir(path):
                os.mkdir(path)
            
            sf.write('%s/%s'%(path,name), mixchannel, 8000)

import os
import random
import scipy.signal as ss
import soundfile as sf
import rir_generator as rir

path = '/home/ed716/Documents/NewSSD/Cocktail/audio/norm_audio_train'
save_path = '/home/ed716/Documents/NewSSD/Cocktail/audio/audio_ch2'
data = os.listdir(path)
for i in range(len(data)):
    data_path = path + '/' + data[i]
    signal, fs = sf.read(data_path, always_2d=True)
    
    with open('ch1.txt') as f:
        source = f.read().splitlines()
    for j in range(len(source)):
        if source[j].split(',')[0] == data[i]:
            x = float(source[j].split(',')[1])
            y = float(source[j].split(',')[2])
            z = float(source[j].split(',')[3])
    
    #x = random.uniform(0.4, 0.5)
    #y = random.uniform(0.4, 0.5)
    #z = random.uniform(1, 1.1)

    h = rir.generate(
        c=340,                  # Sound velocity (m/s)
        fs=fs,                  # Sample frequency (samples/s)
        r=[0.35, 0.3, 1],        # Receiver position(s) [x y z] (m)
        s=[x, y, z],            # Source position [x y z] (m)
        L=[4, 5, 3],            # Room dimensions [x y z] (m)
        reverberation_time=0.4, # Reverberation time (s)
        nsample=4096,           # Number of output samples
    )

    signal = ss.convolve(signal, h)
    name = data[i]
    sf.write('%s/%s'%(save_path,name),signal,8000)
    
    #with open('ch1.txt','a') as f:
    #    name = data[i]
    #    f.write(name + ',' + str(x) + ',' + str(y) + ',' + str(z) + '\n')

import sys
sys.path.append("../../model/lib")
import os
import librosa
import scipy.io.wavfile as wavfile

MIX_PATH = '/home/ed716/Documents/NewSSD/Cocktail/lrs2_spk4_ch1/tt/mix'
SAVE_PATH = '/home/ed716/Documents/NewSSD/Cocktail/lrs2_spk4_ch2/tt/mix'
SINGLE_PATH = '/home/ed716/Documents/NewSSD/Cocktail/audio/test_ch2'
NUM_SPEAKER = 4

def init_dir(path = SAVE_PATH):
    if not os.path.isdir(path):
        os.mkdir(path)

def generate_path_list(mix_path=MIX_PATH):
    mix_speech = os.listdir(mix_path)
    mix = []
    for i in range(len(mix_speech)):
        mix.append(mix_speech[i])
    return mix

def mix_data(mix, num_speaker=NUM_SPEAKER, path=SINGLE_PATH, save_path=SAVE_PATH):
    mix_rate = 1.0 / float(num_speaker)

    for i in range(len(mix)):
        name = mix[i]
        s1path = path + '/' + name[4:29] + '.wav'
        s2path = path + '/' + name[30:55] + '.wav'

        wav1, sr = librosa.load(s1path, sr=8000)
        wav2, sr = librosa.load(s2path, sr=8000)
        mix_wav = wav1 * mix_rate + wav2 * mix_rate

        wavfile.write('%s/%s'%(save_path,name), 8000, mix_wav)

if __name__ == "__main__":
    init_dir()
    mix= generate_path_list()
    mix_data(mix)

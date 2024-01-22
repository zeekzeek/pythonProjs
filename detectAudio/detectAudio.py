from scipy.io import wavfile
samplerate, data = wavfile.read('SkippyPB_82_Drums_4bars.wav')

maxVolume = 0.5
isLoud = False
for i in data:
    if i > maxVolume:
        isLoud = True
        break
if isLoud:
    print('Audio Detected.')

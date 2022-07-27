import matplotlib
matplotlib.use('TkAgg')
import librosa
import librosa.display
import os
import audaugio


def man_to_women_english(file_name):
    directory = os.getcwd()
    # equalizer  man english
    y, sr = librosa.load(directory + "/" + file_name, sr=None)
    print(sr)
    sr = 55000
    chain = audaugio.FlatChain(audaugio.EqualizerAugmentation(27500, .20, 500))
    augmented_audio = chain(y, sr)

    for i, a in enumerate(augmented_audio):
        librosa.output.write_wav("equalizer-" + file_name, a, sr)

    return directory + "/" + "equalizer-" + file_name


def women_to_man_chinese(file_name):
    directory = os.getcwd()
    # # equalizer women to man chinese
    y, sr = librosa.load(directory + "/" + file_name, sr=None)
    sr = 35200

    chain = audaugio.FlatChain(audaugio.EqualizerAugmentation(17600, .20, 500))

    augmented_audio = chain(y, sr)

    for i, a in enumerate(augmented_audio):
        librosa.output.write_wav("equalizer-" + file_name, a, sr)

    return directory + "/" + "equalizer-" + file_name
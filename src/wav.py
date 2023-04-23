import scipy.io.wavfile as wavfile
import numpy as np

import error
import path


def check_directory():
    if not path.wav_files.exists():
        error.yellow_print("wav_files directory not found!")

    wav_files = list(p.name for p in path.wav_files.glob("*.wav"))
    if len(wav_files) == 0:
        error.yellow_print("wav file not found!")

    return wav_files


def load_file(filename):
    try:
        fs, sound_data = wavfile.read(path.wav_files.joinpath(filename))
    except FileNotFoundError:
        error.yellow_print("wav file not found!")

    if len(sound_data.shape) > 1:
        sound_data = np.mean(sound_data, axis=1)

    return fs, sound_data

import json
import numpy as np
import matplotlib.pyplot as plt

import error
import path
import wav


# FFT (高速フーリエ変換) を実行して周波数スペクトルを取得
def fft(data, fs):
    N = len(data)
    fft_data = np.abs(np.fft.fft(data))[:N//2]
    freqs = np.fft.fftfreq(N, d=1.0/fs)[:N//2]
    return freqs, fft_data


# 周波数スペクトルの図表化
def plot(freqs, fft_data):
    plt.plot(freqs, fft_data)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.show()


# ピーク周波数の取得
def get_peak_freq(freqs, fft_data):
    peak_freq = freqs[np.argmax(fft_data)]
    return peak_freq


def get_freq_data():
    try:
        with open(path.parent.joinpath("pitch_frequency_table.json"), "r") as f:
            freq_data = json.load(f)
    except FileNotFoundError:
        error.yellow_print("pitch_frequency_table.json not found!")

    return freq_data


# 音程の取得
def get_nearest_note(freq):
    freq_data = get_freq_data()

    min_dist = np.inf
    nearest_note = ""
    for note, freq_data in freq_data.items():
        dist = abs(freq_data - freq)
        if dist < min_dist:
            min_dist = dist
            nearest_note = note

    return nearest_note


def main():
    wav_files = wav.check_directory()

    print("Wav files:", wav_files)

    for wav_file in wav_files:
        fs, sound_data = wav.load_file(wav_file)

        freqs, fft_data = fft(sound_data, fs)
        peak_freq = get_peak_freq(freqs, fft_data)
        nearest_note = get_nearest_note(peak_freq)

        print("=" * 20)
        print("File name:", wav_file)
        print("Peak frequency:", peak_freq, "Hz")
        print("Nearest note:", nearest_note)
        print("=" * 20)


if __name__ == "__main__":
    main()

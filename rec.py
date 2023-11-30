import sounddevice as sd
from scipy.io.wavfile import write

import whisper
from audio_recorder_streamlit import audio_recorder

def record_audio(duration, file_name):
    fs = 44100   # sampling frequency
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()    # wait for the recording to finish
    write(file_name, fs, recording)     # save the recorded audio



def transcribe_to_text(file_name):

    model = whisper.load_model('base')      # openai SST model
    result = model.transcribe('/Users/sahreenhaider/Downloads/prompt1.m4a')
    return result               # returning the text of transcribed audio



if __name__ == '__main__':
    record_audio(10 ,'/Users/sahreenhaider/Documents/ASK-ME/data/prompt.wav')
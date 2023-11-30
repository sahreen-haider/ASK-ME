import sounddevice as sd
from scipy.io.wavfile import write
import tqdm
import whisper
from audio_recorder_streamlit import audio_recorder

def record_audio(duration, file_name):
    fs = 44100   # sampling frequency
    print('recording.......')
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()    # wait for the recording to finish
    print('recording ended.........')
    write(file_name, fs, recording)     # save the recorded audio



def transcribe_to_text(file_name):
    model = whisper.load_model('base')      # openai SST model
    result = model.transcribe('/Users/sahreenhaider/Documents/ASK-ME/data/prompt.mp3')
    return result["text"]               # returning the text of transcribed audio
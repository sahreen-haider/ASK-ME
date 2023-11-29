import whisper
from audio_recorder_streamlit import audio_recorder

model = whisper.load_model('base')
result = model.transcribe('/Users/sahreenhaider/Downloads/prompt1.m4a')
print(result["text"])
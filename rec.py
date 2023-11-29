import whisper
import whisper

model = whisper.load_model('base')
result = model.transcribe('/Users/sahreenhaider/Downloads/prompt.m4a')
print(result["text"])
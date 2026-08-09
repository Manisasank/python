from gtts import gTTS

Data = ("Hello, this is a text to speech conversion example using gTTS library in Python.")
tts = gTTS(text=Data, lang='en')
tts.save("output.mp3")
print("Text to speech conversion completed. The output is saved as 'output.mp3'.")
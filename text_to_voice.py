from gtts import gTTS

Text = "Hello, this is a text to speech conversion using gTTS library."

tts = gTTS(text=Text, lang='en')
tts.save("voice.mp3")
print("audio saved successfully")
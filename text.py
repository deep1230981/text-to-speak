import pyttsx3.
# initialize Text-to-speech engine.
engine = pyttsx3.init()
# convert this text to speech.
text ="Hi deep the black hat hacker"
engine.say(text)
# play the speech.
engine.runAndWait()
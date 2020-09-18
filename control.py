import speech_recognition as sr
from pynput.keyboard import Key, Controller
import time

class Typing:
    def __init__(self, voiceMessage):
        self.controlKey = self.bindingVoiceOrderToKey(voiceMessage)
    
    def bindingVoiceOrderToKey(self, message):
        self.keyboard = Controller()
        if message == "salta":
            return self.pressAndRelease("w")
        elif message == "agazapa":
            return  self.pressAndRelease("s")
        elif message == "adelante":
            return  self.keyboard.press("d")
        elif message == "atrás":
            return  self.keyboard.press("a")
        elif message == "acción":
            return  self.keyboard.press(Key.shift)
    
    def pressAndRelease(self, key):
        self.keyboard.press(key)
        time.sleep(1)
        self.keyboard.release(key)
        
    
class Recognize:
    def __init__(self):
        self.commandVoice = self.userVoice()
    
    def userVoice(self):
        speech = sr.Recognizer()   
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)            
            audio = speech.listen(source)
        try:
            commandVoice = speech.recognize_google(audio, language = "es-ES").casefold()
            return commandVoice
        except sr.UnknownValueError:
            pass
        except sr.RequestError as error:
            print(error)

def main():
    user = Recognize()
    typing = Typing(user.commandVoice)
    return typing

if __name__ == "__main__":
    try:
        while True:
            main()
    except (KeyboardInterrupt, SystemExit):
        raise

import socket
from vosk import Model, KaldiRecognizer
import pyttsx3
import pyaudio
import json
import nltk
import time
from nltk.tokenize import sent_tokenize
pyttsx_voice_id = 0

def text_to_speech(engine, pyttsx_voice_id, text):

    if not isinstance(text, str):
        text = str(text)
    sentences = sent_tokenize(text)
    
    for sentence in sentences:
        voices = engine.getProperty('voices')
        
        engine.setProperty('voice', voices[pyttsx_voice_id].id)
        engine.say(sentence)
        engine.runAndWait()

    
def Vosk_Voice_to_text(vosk_recognizer):
    
    cap = pyaudio.PyAudio()
    stream = cap.open(input=True, format=pyaudio.paInt16, channels=1, rate=32000, frames_per_buffer=2048)
    stream.start_stream()

    # Verwenden des Mikrofons zum Aufnehmen von Audio
    while True:
        data = stream.read(4096)
        if vosk_recognizer.AcceptWaveform(data):
            text = vosk_recognizer.Result()
            result = json.loads(text)
            vosktext = result['text']
            print(f"Erkannter Text: {vosktext}")
            print(f"Erkannter Text: {vosktext}", 1, "left")  # Füge diese Debugging-Ausgabe hinzu
            print("\033[F\033[K", end="")            
            return vosktext


#'Words to remove von get_user_input(vosk_recognizer)'
words_to_remove = ["paul", "alter", "tom", "mutherfucker", "paolo", "cabeza de melón" ]

def get_user_input(vosk_recognizer):
    while True:
        
        while True:
            input_text = Vosk_Voice_to_text(vosk_recognizer)  # Make sure Vosk_Voice_to_text returns the recognized text
            if input_text:
                print(input_text)
                break  # Exit the loop if there is valid input

        input_text_lower = input_text.lower()

        if any(word in input_text_lower for word in words_to_remove):
            # Use a list comprehension to remove the specified words
            text = ' '.join(word for word in input_text.split() if word.lower() not in words_to_remove)
            return text


def text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, prompt):
    text_to_speech(engine, pyttsx_voice_id, prompt,)
    return get_user_input(vosk_recognizer)

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    dialog_flag = False
    message = ""
    data = ""
    while message.lower().strip() != 'stop':
        print("hallo")
        print(data.lower())
        
        if data.lower() == "dialog aus":
            dialog_flag = False
            
        elif data.lower() == "dialogmodus" or dialog_flag == True:
            dialog_flag = True 

            while True:            
                data = client_socket.recv(1024).decode()
                if data:                
                    break
                time.sleep(0.5) 

            print(data)
            text_to_speech(engine,pyttsx_voice_id, data)

            message = get_user_input(vosk_recognizer) 
            client_socket.send(message.encode())                              
            
        else:
            message = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Was kann ich für dich tun?")
            client_socket.send(message.encode())
            message = ""
            while True:            
                data = client_socket.recv(1024).decode()
                if data:                
                    break
                time.sleep(0.5) 
            print(data)
            text_to_speech(engine,pyttsx_voice_id, data) 
                 
        
        message = ""
        
    client_socket.close()

if __name__ == '__main__':
    engine = pyttsx3.init()
    model = Model(r"zubehoer/vosk-model-small-de-zamia-0.3") 
    vosk_recognizer = KaldiRecognizer(model, 32000)
    client_program()
import configparser #Sorgt dafür das die Config.ini Dateien gelesen werden können
global chatbot
from vosk import Model, KaldiRecognizer
import sys
import Tapo
import tapo_new
import threading
#sys.path.append(r'Lib\site-packages')
import os
from variables_for_all import debug_mode
from variables_for_all import pyttsx_voice_id

import show_functions





def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_voice_assistent():
    clear_console()

#Start print_function
    
def stop_print_function_thread():
    global stop_flag
    global print_function_thread
    if print_functions_thread.is_alive():
        stop_flag = True
        if debug_mode == True:print("Stopping print_functions_thread...")
        print_functions_thread.join()  # Wartet darauf, dass der Thread beendet wird
        if debug_mode == True:print("print_functions_thread stopped.")            
    else:
        if debug_mode == True:print("print_functions_thread is not running.")       
        

def call_print_function_thread(debug_mode):
    global print_functions_thread
    functions = function_collection(0)    
    print_functions_thread = threading.Thread(target=print_functions,  args=(functions, debug_mode,))
    print_functions_thread.start()
    #stop_print_functions_thread = threading.Thread(target=stop_print_function_thread, daemon=True, args=(print_functions_thread))
    #stop_print_functions_thread.start()
    
def print_functions(functions, debug_mode,): 
    global stop_flag
    stop_flag = False
    while not stop_flag: 
        if debug_mode == True:print("print_functions: \n Stop_Flag: " + str(stop_flag))
        # Choose a random function from the list
        random_function = random.choice(functions)
        
        sentence_start = random_function[0]
        sentence_end = random_function[1]
        word = random_function[2]        
        and_word = random_function[3]
        function_description = random_function[4]

        if function_description is not None and len(function_description) >= 3:
            text_1, text_2, text_3 = show_functions.colorize_signal_words(sentence_start, sentence_end, word, and_word, function_description, color=show_functions.ConsoleColors.GREEN)
            anzeigen_und_ausblenden(text_1, text_2, text_3, speed=4)
            #if debug_mode == True:funktions.clear_voice_assistent()
        elif stop_flag == True:
            break
        else:
            continue
    


def function_collection(pyttsx_voice_id):
    config = configparser.ConfigParser()
    if pyttsx_voice_id == 0:
        additional_config_paths = [
                resource_path('config/German_app_config.ini'),
                resource_path('config/German_tapo_config.ini'),
                resource_path('config/German_chat_config.ini'),
                resource_path('config/German_combination_config.ini')            
            ]
        config.read(additional_config_paths)
        
    elif pyttsx_voice_id == 2:
        additional_config_paths = [            
                resource_path('config/English_app_config.ini'),
                resource_path('config/English_tapo_config.ini'),
                resource_path('config/English_chat_config.ini'),
                resource_path('config/English_combination_config.ini')
                ]    
        config.read(additional_config_paths)

    elif pyttsx_voice_id == 4:
        additional_config_paths = [            
                resource_path('config/Spanish_app_config.ini'),
                resource_path('config/Spanish_tapo_config.ini'),
                resource_path('config/Spanish_chat_config.ini'),
                resource_path('config/Spanish_combination_config.ini'),
                # Füge hier die Pfade für die restlichen Config-Dateien hinzu
            ]
        config.read(additional_config_paths)

    function_collection_list = []    

    for i in range(1, 16):
        section_name = f'ChatSettings Funktion {i}'  
        function_description = config.get(section_name, 'function_description')
        example_sentence_start = config.get(section_name, 'example_sentence_start')
        example_sentence_end = config.get(section_name, 'example_sentence_end')
        signal_words = config.get(section_name, 'signal_words')
        and_signal_words = config.get(section_name, 'and_signal_words')
        chat_function = example_sentence_start, example_sentence_end, signal_words, and_signal_words, function_description
        #if debug_mode == True:print(str(chat_function))
        #if debug_mode == True:print("***************************************************************************************************")

        app_section_name = f'AppSettings Funktion {i}'
        app_function_description = config.get(app_section_name, 'app_function_description')
        app_example_sentence_start = config.get(app_section_name, 'app_example_sentence_start')
        app_example_sentence_end = config.get(app_section_name, 'app_example_sentence_end')
        app_signal_words = config.get(app_section_name, 'app_signal_words')
        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
        app_function = app_example_sentence_start, app_example_sentence_end, app_signal_words, app_and_signal_words, app_function_description
        #if debug_mode == True:print(str(app_function))
        #if debug_mode == True:print("***************************************************************************************************")

        tapo_section_name = f'TapoSettings_Funktion_{i}'
        tapo_function_description = config.get(tapo_section_name, 'tapo_function_description')
        tapo_example_sentence_start = config.get(tapo_section_name, 'tapo_example_sentence_start')
        tapo_example_sentence_end = config.get(tapo_section_name, 'tapo_example_sentence_end')
        tapo_signal_words = config.get(tapo_section_name, 'tapo_signal_word')
        tapo_and_signal_words = config.get(tapo_section_name, 'tapo_and_signal_word') 
        tapo_function = tapo_example_sentence_start, tapo_example_sentence_end, tapo_signal_words, tapo_and_signal_words, tapo_function_description  
        #if debug_mode == True:print(str(tapo_function))
        #if debug_mode == True:print("***************************************************************************************************")

        combination_section_name = f'CombinationSettings_Funktion_{i}'
        combination_function_description = config.get(combination_section_name, 'combination_function_description')
        combination_example_sentence_start = config.get(combination_section_name, 'combination_example_sentence_start')
        combination_example_sentence_end = config.get(combination_section_name, 'combination_example_sentence_end')
        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
        combination_function = combination_example_sentence_start, combination_example_sentence_end, combination_signal_words, combination_and_signal_words, combination_function_description
        #if debug_mode == True: print(str(combination_function))
        #if debug_mode == True:print("***************************************************************************************************")

        function_collection_list.extend([chat_function, app_function, tapo_function, combination_function])

    return function_collection_list


import ctypes  
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

def anzeigen_und_ausblenden(text_1, text_2, text_3, speed=5):
    global stop_flag
    terminal_breite, terminal_hoehe = shutil.get_terminal_size()

    sichtbare_zeilen = min(terminal_hoehe, 30)

    text_1_breite = 40 + len(text_1)
    text_1_hoehe = text_1.count('\n') + 10

    # Positionen so wählen, dass der gesamte Text sichtbar bleibt
    #position_x = random.randint(40, max(40, terminal_breite - text_1_breite))
    #position_y = random.randint(10, max(10, sichtbare_zeilen - text_1_hoehe))
    position_x_1 = (terminal_breite // 2) - (len(text_1) // 2)
    position_y_1 = (sichtbare_zeilen // 2)
    position_x_2 = (terminal_breite // 2) - (len(text_2) // 2)
    position_y_2 = (sichtbare_zeilen // 2)
    position_x_3 = (terminal_breite // 2) - (len(text_3) // 2)
    position_y_3 = (sichtbare_zeilen // 2)
    position_1 = COORD(position_x_1, position_y_1)
    position_2 = COORD(position_x_2, position_y_2)
    position_3 = COORD(position_x_3, position_y_3)

    # Get console handle
    h = ctypes.windll.kernel32.GetStdHandle(-11)
    if stop_flag == False:
        print(' ' * terminal_breite, end='\r')
        # Set console cursor position for text_1
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_3)

        # Einblenden text_1
        print(text_3, end='\r')

        time.sleep(2)  # 5 Sekunden anzeigen lassen

        # Ausblenden text_1
        print(' ' * terminal_breite, end='\r')

        # Koordinaten reset
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))
        pass

    if stop_flag == False:
        # Set console cursor position for text_2
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_1)
        # position_2 = COORD(position_x, position_y + text_1_hoehe)
        #ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_2)

        # Einblenden text_2
        print(text_1, end='\r')

        time.sleep(speed)  # 5 Sekunden anzeigen lassen

        # Ausblenden text_2
        print(' ' * terminal_breite, end='\r')

        # Koordinaten reset
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))
        pass

    if stop_flag == False:
        # Set console cursor position for text_1
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_2)

        # Einblenden text_1
        print(text_2, end='\r')

        time.sleep(speed)  # 5 Sekunden anzeigen lassen

        # Ausblenden text_1
        print(' ' * terminal_breite, end='\r')

        # Koordinaten reset
        ctypes.windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))
        pass

#End print_function


def resource_path(relative_path):
    import os
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        #PyInstaller creates a temp folder and stores path in MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Text formatierung in Console Anfang
import shutil

def scroll_console():
    rows, _ = shutil.get_terminal_size()   
    # Scrollen durch Zeilenumbrüche
    for _ in range(rows//2):
        print("\n", end="")
        #time.sleep(0.05)  # kurze Pause zwischen den Zeilen für die Sichtbarkeit

def print_at_bottom(text):
    terminal_breite, terminal_hoehe = shutil.get_terminal_size()
    # Den Text am unteren Ende platzieren (zweite letzte Zeile)
    zeile = terminal_hoehe - 2
    print("\033[{};{}H{}".format(zeile, 0, text))

def print_center_zeile(text, zeile, format):   
    terminal_breite, _ = shutil.get_terminal_size()
    zeile = int(zeile)
    zentrierter_text = text.center(terminal_breite)
    if format == "left":
        print("\033[{};{}H{}".format(zeile, 0, text))
    elif format == "center":        
        print("\033[{};{}H{}".format(zeile, 0, zentrierter_text))
    elif format == "right":
        print("\033[{};{}H{}".format(zeile, 3, text))    
    
def set_cursor_to_line(zeile):
    print("\033[{};0H".format(zeile))
#Text formatierung in Console Anfang

# Spracherkennung mit Vosk und User_Input Anfang
import pyaudio
import json

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
            if debug_mode == True:print(f"Erkannter Text: {vosktext}")
            if debug_mode == False:print_center_zeile(f"Erkannter Text: {vosktext}", 1, "left")  # Füge diese Debugging-Ausgabe hinzu
            if debug_mode == False:print("\033[F\033[K", end="")            
            return vosktext


#'Words to remove von get_user_input(vosk_recognizer)'
words_to_remove = ["paul", "alter", "tom", "mutherfucker", "paolo", "cabeza de melón" ]

def get_user_input(vosk_recognizer):
    while True:
        
        while True:
            input_text = Vosk_Voice_to_text(vosk_recognizer)  # Make sure Vosk_Voice_to_text returns the recognized text
            if input_text:
                if debug_mode == True: print(input_text)
                break  # Exit the loop if there is valid input

        input_text_lower = input_text.lower()

        if any(word in input_text_lower for word in words_to_remove):
            # Use a list comprehension to remove the specified words
            text = ' '.join(word for word in input_text.split() if word.lower() not in words_to_remove)
            return text


def text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, prompt):
    text_to_speech(engine, pyttsx_voice_id, prompt,)
    return get_user_input(vosk_recognizer)


def confirm_response(engine, vosk_recognizer, prompt):
    while True:
        user_input = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, prompt)
        text_to_speech(engine, pyttsx_voice_id, "Hast du" + user_input +"gesagt")
        user_input_check = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Bitte antworte mit Ja oder Nein.")
        if debug_mode == True: print(user_input_check)
        if "nein" in user_input_check.lower():
            text_to_speech(engine, pyttsx_voice_id, "Entschuldigung, ich habe dich nicht richtig verstanden. Bitte wiederhole deine Antwort.")
        else:
            return user_input
# Spracherkennung mit Vosk und User_Input Ende


# Funktion für abwechselungsreiche Sätze/ Sprache des Assistenten Anfang
import random
file_path_satz = resource_path('Sätze.txt') #Pfad zu den Random Sätzen
def get_random_sentence_from_file(file_path_satz, marker):
    try:
        with open(file_path_satz, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(marker):
                    sentences = line[len(marker):].strip().split(', ')
                    # Zufällig einen Satz auswählen
                    random_sentence = random.choice(sentences)
                    return random_sentence
    except FileNotFoundError:
        if debug_mode == True: print(f"Die Datei {file_path_satz} wurde nicht gefunden.")
        return None
    except Exception as e:
        if debug_mode == True: print(f"Fehler beim Lesen der Datei {file_path_satz}: {e}")
        return None

# Funktion für abwechselungsreiche Sätze/ Sprache des Assistenten Ende

# (noch nicht eingebaut und genutzt)
# Funktion zum checken der Sprache der Antworten von Huggingface Anfang
def check_language(antwort):
    global lang

    # Erstelle eine Liste mit Wörtern, die typischerweise in Englisch verwendet werden
    english_words = ["the", "of", "and", "to", "a", "in", "that", "is", "it"]

    # Erstelle eine Liste mit Wörtern, die typischerweise in Deutsch verwendet werden
    german_words = ["der", "die", "das", "und", "zu", "ein", "in", "das", "ist"]

    # Zähle die Anzahl der Wörter in jeder Liste, die in der Antwort enthalten sind
    english_count = 0
    german_count = 0
    for word in antwort.split():
        if word in english_words:
            english_count += 1
        elif word in german_words:
            german_count += 1

    # Wenn die Anzahl der englischen Wörter größer ist als die Anzahl der deutschen Wörter,
    # dann ist die Antwort wahrscheinlich Englisch
    if english_count > german_count:
        lang = "en"
        return lang
    else:
        lang = "de"
        return lang

def ask_for_translation(lang, antwort):
    global translation
    # Assuming you have a method in your ChatBot class to request translations
    if lang == "en":
        translation = hugchat("Bitte übersetze mir folgendes auf deutsch: " + antwort + " Die Antwort soll kein englisches Wort enthalten und nur den übersetzten Text enthalten", chatbot)
        return translation
    else:
        translation = antwort
        return translation

# Funktion zum checken der Sprache der Antworten von Huggingface Ende



#Huggingface Anfang

# Importieren der HugChat-Klassen
from hugchat.hugchat import ChatBot
from hugchat.login import Login

import textwrap


def initialize_huggingface():
    
    try:
        # Einloggen bei Huggingface und Autorisieren von HugChat
        sign = Login("sandburg.registrierung@mail.de", "Strand42!")
        cookies = sign.login()
        if debug_mode == True: print(cookies)
        # Cookies im lokalen Verzeichnis speichern
        cookie_path_dir = resource_path("./cookies_snapshot")
        sign.saveCookiesToDir(cookie_path_dir)
        # Neue HugChat-Verbindung starten
        chatbot = ChatBot(cookies=cookies)

        return chatbot
    except Exception as e:
        if debug_mode == True: print(f"Fehler bei der Initialisierung von Huggingface: {e}")
        return None

# Funktion für die Interaktion mit HugChat
def hugchat(user_input, chatbot):
    if chatbot is None:
        if debug_mode == True: print("Huggingface konnte nicht initialisiert werden.")
        return "Ich konnte keine Antwort von HugChat erhalten."

    if debug_mode == True: print(f"Versuche mit HugChat zu chatten: {user_input}")

    # Nachricht eingeben
    msg = user_input
    antwort = chatbot.chat(msg)

    if antwort is None:
        if debug_mode == True: print("HugChat hat keine gültige Antwort geliefert.")
        return "Ich konnte keine Antwort von HugChat erhalten."

    # Extrahiere den Textinhalt aus dem Message-Objekt
    antwort_text = antwort.content if hasattr(antwort, 'content') else str(antwort)
    scroll_console()
    if debug_mode == False:clear_voice_assistent()
    set_cursor_to_line(5)
    print(antwort_text)

    return antwort_text


def huggingfacechat(engine, user_input, chatbot, pyttsx_voice_id):
    # Einstellungen für die Antwortlänge festlegen
    antwort = hugchat(user_input, chatbot)
    if pyttsx_voice_id == 0:
        check_language(antwort)
        if debug_mode == True: print(lang)
        ask_for_translation(lang, antwort)
        antwort = translation
        #print_sentences(antwort)   
        text_to_speech(engine, pyttsx_voice_id, antwort)
    elif pyttsx_voice_id == 2:
        text_to_speech(engine, pyttsx_voice_id, antwort)
    elif pyttsx_voice_id == 4:
        text_to_speech(engine, pyttsx_voice_id, antwort)


def huggingface_newchat(chatbot):
    try:
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        return chatbot
    except Exception as error:
        if debug_mode == True: print(f"Error in huggingface_newchat: {error}")
        raise error



# Huggingface Ende

# Bingchat Anfang


import asyncio
import json
from pathlib import Path

import textwrap

async def ask_copilot(user_input: str) -> str:
   bot = None
   try:
      from re_edge_gpt import Chatbot, ConversationStyle
      mode = "Copilot"
      if mode == "Bing":
         cookies: list[dict] = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
      else:
         cookies: list[dict] = json.loads(open(
            str(Path(str(Path.cwd()) + "/copilot_cookies.json")), encoding="utf-8").read())
      # Notice when mode != "Bing" (Bing is default) will set mode is copilot
      bot = await Chatbot.create(cookies=cookies)
      #bot = await Chatbot.create(cookies=cookies, mode=mode)
      response = await bot.ask(
         prompt=user_input,
         conversation_style=ConversationStyle.balanced,
         simplify_response=True
      )
      # If you are using non ascii char you need set ensure_ascii=False
      print(json.dumps(response, indent=2, ensure_ascii=False))
      # Raw response
      # print(response)
      assert response
   except Exception as error:
        if debug_mode == True: print(f"Error in ask_copilot: {error}")
        raise error
   finally:
      if bot is not None:
         await bot.close()

async def ask_bingchatbot(user_input: str) -> str:
    bot = None
    try:
        from re_edge_gpt import Chatbot, ConversationStyle
        cookies = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies_chat.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt=user_input,
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        text_result = response.get("text", "")
        cleaned_text = text_result.replace("*", "").replace("[^1^]", "").replace("[^3^]", "")
        sources_text = response.get("sources_text", "")
        cleaned_sources = sources_text.replace("Learn more: [1.", "").replace("](", "").replace(") [2.", "").replace(
            ") [3.", "").replace(") [4.", "").replace(") [5.", "").replace(") [6.", "").replace(") [7.", "").replace(
            ") [8.", "").replace(") [9.", "").replace(") [10.", "")
        return cleaned_text, cleaned_sources
    except Exception as error:
        if debug_mode == True: print(f"Error in ask_bingchatbot: {error}")
        raise error
    finally:
        if bot is not None:
            await bot.close()

def copilot(engine, user_input: str) -> None:
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()

    text_result, sources_text = loop.run_until_complete(ask_copilot(user_input))

    if debug_mode == True: print("Ergebnis:")
    print(text_result)
    #print_sentences(text_result)

    if debug_mode == True: print("\nQuellenangabe:")
    print(sources_text)
    #print_sentences(sources_text)
    text_to_speech(engine, pyttsx_voice_id, text_result)


def bingchat(engine, user_input: str) -> None:
    try:
        loop = asyncio.get_running_loop()
        if debug_mode == True:print("bingchat: Loop läuft")
    except RuntimeError:
        if debug_mode == True:print("bingchat: Looperror")
        loop = asyncio.get_event_loop()

    text_result, sources_text = loop.run_until_complete(ask_bingchatbot(user_input))

    if debug_mode == True: print("Ergebnis:")
    print(text_result)
    #print_sentences(text_result)

    if debug_mode == True: print("\nQuellenangabe:")
    print(sources_text)
    #print_sentences(sources_text)
    text_to_speech(engine, pyttsx_voice_id, text_result)


# Bingchat Ende

# Perplexity Anfang
from perplexity import Perplexity

def perplexity_new(engine, user_input):
    perplexity = Perplexity()
    answer = perplexity.search(user_input)
    full_answer = ""
    last_chunk = ""
    for item in answer:
        if 'answer' in item and item['answer']:
            current_chunk = item['answer']
            if current_chunk.startswith(last_chunk):
                new_content = current_chunk[len(last_chunk):]
                full_answer += new_content
            else:
                full_answer += current_chunk
            last_chunk = current_chunk

            if 'final' in item and item['final']:
                break

    if full_answer:
        formatted_answer = textwrap.fill(full_answer, width=10000)
        formatted_answer = formatted_answer.replace('-', '\n   -')  # Add a new line before each dash
        formatted_answer = formatted_answer.rsplit('\n', 1)
        if len(formatted_answer) == 2:
            last_line = formatted_answer[1]
            last_line = last_line.replace('  ', '\n')  # Add a new line before each double space
            formatted_answer = [formatted_answer[0], last_line]
        formatted_answer = ''.join(formatted_answer)
        formatted_answer = formatted_answer.replace('##', '\n')  # Add a new line before each ## and erase them
        print(formatted_answer)
        text_to_speech(engine, pyttsx_voice_id, formatted_answer)
    else:
        print("No valid results found")
    
    #HAlloperplexity.close()




# Perplexity Ende

# Spotify Anfang

# Hier werden erforderliche Bibliotheken importiert
import pyautogui  # Bibliothek zur Automatisierung von Maus- und Tastatureingaben
import os  # Bibliothek zum Aufrufen von Systembefehlen
import time  # Bibliothek für Zeitverzögerungen

def is_app_open(app):
    # Gibt die Position des Anwendungsfensters zurück, wenn es gefunden wird, andernfalls None.
    app_position = pyautogui.locateOnScreen(app)
    if app_position:
        return True
    else:
        return False


import ast

def app_ultimate(app, mouse_click_on_coordinates_, double_mouse_click_on_coordinates_, hotkey_tups, waits, texts, keys_lists, user_input_enabled, user_input_app, engine):
    os.system(app)
    if debug_mode == True: print(app)
    time.sleep(waits[0])
    print("app_ultimate")
    for i in range(1, 7):
        if mouse_click_on_coordinates_[i - 1].strip():
            x, y = map(int, mouse_click_on_coordinates_[i - 1].split(','))
            pyautogui.click(x, y)

        if double_mouse_click_on_coordinates_[i - 1].strip():
            x, y = map(int, double_mouse_click_on_coordinates_[i - 1].split(','))
            pyautogui.doubleClick(x, y)

        pyautogui.hotkey(*hotkey_tups[i - 1])
        if debug_mode == True: print(f"Pressed hotkey: {hotkey_tups[i - 1]}")
        time.sleep(waits[i * 3 - 2])

        if user_input_enabled[i - 1] and user_input_app:
            pyautogui.write(user_input_app)
            if debug_mode == True: print(f"Wrote user input: {user_input_app}")
        elif not user_input_enabled[i - 1]:
            pyautogui.write(texts[i - 1])
        elif user_input_enabled[i - 1]:
            text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
            if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")

        time.sleep(waits[i * 3 - 1])

        for key in keys_lists[i - 1]:
            time.sleep(waits[i * 3])
            pyautogui.press(key)
            if debug_mode == True: print(f"Pressed key: {key}")



def app_ultimate_old (app, mouse_click_on_coordinates_1, double_mouse_click_on_coordinates_1, 
                                               mouse_click_on_coordinates_2, double_mouse_click_on_coordinates_2, mouse_click_on_coordinates_3, 
                                               double_mouse_click_on_coordinates_3, mouse_click_on_coordinates_4, double_mouse_click_on_coordinates_4, 
                                               mouse_click_on_coordinates_5, double_mouse_click_on_coordinates_5, mouse_click_on_coordinates_6, 
                                               double_mouse_click_on_coordinates_6, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, 
                                               hotkey_5_tup, hotkey_6_tup, wait_app, wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, 
                                    wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                    wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3,
                                    text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                    keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list,
                                    user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                    user_input_enabled_4, user_input_enabled_5, user_input_enabled_6,
                                    user_input_app, engine):
    os.system(app)  # Startet Spotify
    if debug_mode == True: print(app)
    time.sleep(wait_app)  # Wartet 2 Sekunden, um Spotify vollständig zu starten
    if debug_mode == True: print("1")
    #if not pyautogui.locateOnScreen(resource_path('/zubehoer/offene_apps_erkennen_pngs/Spotify_back_button.png')):
    if mouse_click_on_coordinates_1.strip():        
        x, y = map(int, mouse_click_on_coordinates_1.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_1.strip():
        x, y = map(int, double_mouse_click_on_coordinates_1.split(','))
        pyautogui.doubleClick(x, y)
    if debug_mode == True: print(user_input_app)
    pyautogui.hotkey(*hotkey_1_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_1_tup}")
    time.sleep(wait_1_1)

    if user_input_enabled_1 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_1 == False:
        pyautogui.write(text_1)
    
    elif user_input_enabled_1:                                   #Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine SprachanweisunFgen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_1_2)
    
    for key in keys_1_list:
        time.sleep(wait_1_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_1_3)
    if mouse_click_on_coordinates_2.strip():        
        x, y = map(int, mouse_click_on_coordinates_2.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_2.strip():
        x, y = map(int, double_mouse_click_on_coordinates_2.split(','))
        pyautogui.doubleClick(x, y)
    pyautogui.hotkey(*hotkey_2_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_2_tup}")
    time.sleep(wait_2_1)

    if user_input_enabled_2 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_2 == False:
        pyautogui.write(text_2)
        
    elif user_input_enabled_2:                                   #Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_2_2)

    for key in keys_2_list:
        time.sleep(wait_2_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_2_3)
    if mouse_click_on_coordinates_3.strip():        
        x, y = map(int, mouse_click_on_coordinates_3.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_3.strip():
        x, y = map(int, double_mouse_click_on_coordinates_3.split(','))
        pyautogui.doubleClick(x, y)
    pyautogui.hotkey(*hotkey_3_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_3_tup}")
    time.sleep(wait_3_1)

    if user_input_enabled_3 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_3 == False:
        pyautogui.write(text_3)
        
    elif user_input_enabled_3:  # Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_3_2)

    for key in keys_3_list:
        time.sleep(wait_3_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_3_3)
    if mouse_click_on_coordinates_4.strip():        
        x, y = map(int, mouse_click_on_coordinates_4.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_4.strip():
        x, y = map(int, double_mouse_click_on_coordinates_4.split(','))
        pyautogui.doubleClick(x, y)
    pyautogui.hotkey(*hotkey_4_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_4_tup}")
    time.sleep(wait_4_1)

    if user_input_enabled_4 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_4 == False:
        pyautogui.write(text_4)
                
    elif user_input_enabled_4:  # Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_4_2)

    for key in keys_4_list:
        time.sleep(wait_4_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_4_3)
    
    if mouse_click_on_coordinates_5.strip():        
        x, y = map(int, mouse_click_on_coordinates_5.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_5.strip():
        x, y = map(int, double_mouse_click_on_coordinates_5.split(','))
        pyautogui.doubleClick(x, y)
    pyautogui.hotkey(*hotkey_5_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_5_tup}")
    time.sleep(wait_5_1)

    if user_input_enabled_5 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_5 == False:
        pyautogui.write(text_5)
        
    elif user_input_enabled_5:  # Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_5_2)

    for key in keys_5_list:
        time.sleep(wait_5_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_5_3)

    if mouse_click_on_coordinates_6.strip():        
        x, y = map(int, mouse_click_on_coordinates_6.split(','))
        pyautogui.click(x, y)
    if double_mouse_click_on_coordinates_6.strip():
        x, y = map(int, double_mouse_click_on_coordinates_6.split(','))
        pyautogui.doubleClick(x, y)
    pyautogui.hotkey(*hotkey_6_tup)
    if debug_mode == True: print(f"Pressed hotkey: {hotkey_6_tup}")
    time.sleep(wait_6_1)

    if user_input_enabled_6 and user_input_app:
        pyautogui.write(user_input_app)
        if debug_mode == True: print(f"Wrote user input: {user_input_app}")
    elif user_input_enabled_6 == False:
        pyautogui.write(text_6)
        
    elif user_input_enabled_6:  # Wenn user_input = True in app_config.ini dann Text_to_speech.....Code ergänzen!!!
        text_to_speech(engine, pyttsx_voice_id, "Bitte ergänze deine Sprachanweisungen.")
        if debug_mode == True: print("Bitte ergänze deine Sprachanweisungen.")
    time.sleep(wait_6_2)

    for key in keys_6_list:
        time.sleep(wait_6_3)
        pyautogui.press(key)
        if debug_mode == True: print(f"Pressed key: {key}")
    time.sleep(wait_6_3)

#Gibt einen gegebenen Text in der Form aus, dass dies Pro Zeile einen vollständigen Satz ausgibt.
def print_sentences(text):
    if text is None:
        if debug_mode == True: print("The text variable is None.")
    else:
        zeile = 5
        sentences = text.split(".")
        for sentence in sentences:
            print_center_zeile(sentence, zeile, "left")
            zeile += 1


# Diese Funktion gibt die Wörter, die auf ein bestimmtes Wort in der Benutzereingabe folgen, zurück
def naechste_woerter_nach_wort(user_input, app_signal_words, app_and_signal_words):
    woerter = user_input.split()  # Zerlegt die Benutzereingabe in Wörter
    if debug_mode == True: print(woerter)
    if debug_mode == True: print(app_and_signal_words)
    if debug_mode == True: print(app_signal_words)

    try:
        if app_and_signal_words in woerter:
            
            index = woerter.index(app_and_signal_words)  # Findet den Index des gesuchten Wortes
            if debug_mode == True: print(str(index + 1) + "1")
        else:

            
            index = woerter.index(app_signal_words)  # Findet den Index des gesuchten Wortes
            if debug_mode == True: print(str(index + 1) + "2")


        # Überprüft, ob genügend folgende Wörter vorhanden sind
        if index + 1 < len(woerter):  # Hier wird "+1" verwendet, um das erste folgende Wort zu ignorieren
            naechste_woerter = woerter[index + 1:]
            if debug_mode == True: print("nächste Wörter: " + ' '.join(naechste_woerter))
            return ' '.join(naechste_woerter)
        else:
            if debug_mode == True: print("Das gesuchte Wort hat nicht genügend folgende Wörter.")
            return None
    except ValueError:
        if debug_mode == True: print("Das Signalwort wurde nicht gefunden.")
        return None


# Diese Funktion extrahiert den relevanten Teil der Benutzereingabe für die Spotify-Funktionen

def input_app(user_input, app_signal_words, app_and_signal_words):
    ergebnis = naechste_woerter_nach_wort(user_input, app_signal_words, app_and_signal_words)
    if debug_mode == True: print(ergebnis)
    if ergebnis:
        return ''.join(ergebnis)
    else:
        return None

# Spotify Ende


# Text to Speech Funktion Anfang
import nltk
from nltk.tokenize import sent_tokenize
import keyboard
#nltk.download('punkt')

def text_to_speech(engine, pyttsx_voice_id, text):
    global stop_reading

    if not isinstance(text, str):
        text = str(text)
    sentences = sent_tokenize(text)
    stop_reading = False

    def check_escape_key():
        global stop_reading
        while not stop_reading:
            if keyboard.is_pressed('backspace'):
                if debug_mode == False: 
                    print_center_zeile("Vorlesen abgebrochen.", 1, "left")
                if debug_mode == True: 
                    print("Vorlesen abgebrochen.")
                stop_reading = True
                break

    escape_thread = threading.Thread(target=check_escape_key, daemon=True)
    escape_thread.start()

    for sentence in sentences:
        if stop_reading:
            break
        voices = engine.getProperty('voices')
        
        engine.setProperty('voice', voices[pyttsx_voice_id].id)
        engine.say(sentence)
        engine.runAndWait()

    stop_reading = True  # Beende das Vorlesen, wenn der Text fertig gelesen wurde

    # Warte darauf, dass der escape_thread beendet ist
    if escape_thread.is_alive():
        escape_thread.join()
# Text to Speech Funktion Anfang


#Kombination von Funktionen aus Licht, Apps und GPT´s zu neuer Funktion

#def combination():


# Voice Assistent Logik und Funktionsimplementierungen Anfang

active_chat_engine = "huggingface"

#Die Funktion process_user_input() weißt den Input aus den Funktionen von chat_dialog() den GPT zu und gibt die Ergebnisse aus.def process_user_input(engine, active_chat_engine, user_input, chatbot):
def process_user_input(engine, active_chat_engine, user_input, chatbot, pyttsx_voice_id):
    if debug_mode == True: print("Active Chat Engine:", active_chat_engine)
    if debug_mode == True: print("User Input:", user_input)
    """if pyttsx_voice_id == 0:
        text_to_speech(engine, pyttsx_voice_id, "Gerne, einen Moment bitte")
    elif pyttsx_voice_id == 2:
        text_to_speech(engine, pyttsx_voice_id, "Your welcome, one moment please")
    elif pyttsx_voice_id == 4:
        text_to_speech(engine, pyttsx_voice_id, "Sie claro, un momento por favor")"""
    if active_chat_engine.lower() == 'huggingface':
        huggingfacechat(engine, user_input, chatbot, pyttsx_voice_id)
        if debug_mode == True: print("higgingfacechat fertig")
    elif active_chat_engine.lower() == 'bing':
        bingchat(engine, user_input)
    elif active_chat_engine.lower() == 'perplexity':
        perplexity_new(engine, user_input)
    elif active_chat_engine.lower() == 'copilot':
        copilot(engine, user_input)
        

    else:
        if debug_mode == True: print("Unrecognized chat engine")
        if debug_mode == True: print("higgingfacechat richtig fertig")
    

#Beleuchtung Anfang
from PyP100 import PyP100
from PyP100 import PyL530
"""""
def ultimate_light_old(strahler_1, strahler_2, strahler_3, strahler_4, plug_1, plug_2, plug_3, plug_4, strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                   strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color, anschalten_strahler_1_3_color,
                   anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht, anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                   anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4, ausschalten_plug,
                   startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                   color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait):
    try:
        if strahler_color_strobe_multi == True:
            Tapo.strahler_color_strobe_multi(strahler_1, startfarbe_d1, brightness_d1, strahler_2, startfarbe_d2, brightness_d2, strahler_3,
                                        startfarbe_d3, brightness_d3, strahler_4, startfarbe_d4, brightness_d4, color_distanz, wait)
        elif strahler_color_fade_multi == True:
            Tapo.strahler_color_fade_multi(strahler_1, startfarbe_d1, brightness_d1, strahler_2, startfarbe_d2, brightness_d2, strahler_3,
                                        startfarbe_d3, brightness_d3, strahler_4, startfarbe_d4, brightness_d4, color_distanz, wait)
        elif strahler_slow_fade_out == True:
            Tapo.strahler_slow_fade_out(strahler_1, strahler_2, strahler_3, strahler_4, dimmzielwert, dimm_geschwindigkeit, brightness)
        elif strahler_speed_fade_out == True:
            Tapo.strahler_speed_fade_out(strahler_1, strahler_2, strahler_3, strahler_4, dimmzielwert, dimm_geschwindigkeit, brightness)
        elif anschalten_strahler_multi_color == True:
            Tapo.anschalten_strahler_multi_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung)
        elif anschalten_strahler_2_4_color == True:
            Tapo.anschalten_strahler_2_4_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung)
        elif anschalten_strahler_1_3_color == True:
            Tapo.anschalten_strahler_1_3_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung)
        elif anschalten_strahler_multi_licht == True:
            Tapo.anschalten_strahler_multi_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp)
        elif anschalten_strahler_2_4_licht == True:
            Tapo.anschalten_strahler_2_4_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp)
        elif anschalten_strahler_1_3_licht == True:
            Tapo.anschalten_strahler_1_3_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp)
        elif ausschalten_strahler == True:
            Tapo.ausschalten_strahler(strahler_1, strahler_2, strahler_3, strahler_4)
        elif anschalten_plug_multi == True:
            Tapo.anschalten_plug_multi(plug_1, plug_2, plug_3, plug_4)
        elif anschalten_plug_2_4 == True:
            Tapo.anschalten_plug_2_4(plug_2, plug_4)
        elif anschalten_plug_1_3 == True:
            Tapo.anschalten_plug_1_3(plug_1, plug_3)
        elif anschalten_plug_1 == True:
            Tapo.anschalten_plug_1(plug_1)
        elif anschalten_plug_2_3_4 == True:
            Tapo.anschalten_plug_2_3_4(plug_2, plug_3, plug_4)
        elif ausschalten_plug == True:
            ausschalten_plug(plug_1, plug_2, plug_3, plug_4)
    except:
        if debug_mode == True: print("ultimate_light" + f"Error: {e}")"""

def ultimate_light(tapo_section_name, anschalten_lamp_color,
                   startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                   color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait):
    print("ULTIMATE_LIGHT: ", brightness, farbton, saettigung)
    config = configparser.ConfigParser()

    if pyttsx_voice_id == 0:
        config.read(resource_path('config/German_tapo_config.ini'))  
    if pyttsx_voice_id == 2:
        config.read(resource_path('config/English_tapo_config.ini'))  
    if pyttsx_voice_id == 4:
        config.read(resource_path('config/Spanish_tapo_config.ini'))  


    try:
        if anschalten_lamp_color == True:
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'anschalten_lamp_color_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            tapo_new.anschalten_lampe_color(*lamps_involved_list, brightness, farbton, saettigung)

        
    except:
        if debug_mode == True: print("ultimate_light" + f"Error: {e}")        

    
    print("Beteiligte Lampen:", lamps_involved_list)            
#Beleuchtung Ende
#Combinations Anfang

def ultimate_combination(user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
                                            user_combination_input_7, user_combination_input_8, user_combination_input_9, user_combination_input_10, signal_words, and_signal_words, section_name, dialog_chat_enabled, 
                                            app_signal_words, app_and_signal_words, app_section_name, app, mouse_click_on_coordinates_1, mouse_click_on_coordinates_2, mouse_click_on_coordinates_3, 
                                               mouse_click_on_coordinates_4, mouse_click_on_coordinates_5, mouse_click_on_coordinates_6, 
                                               double_mouse_click_on_coordinates_1, double_mouse_click_on_coordinates_2,
                                               double_mouse_click_on_coordinates_3, double_mouse_click_on_coordinates_4, 
                                               double_mouse_click_on_coordinates_5, double_mouse_click_on_coordinates_6, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup, wait_app,
                                            wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                            wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3, text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                            keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list, user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                            user_input_enabled_4, user_input_enabled_5, user_input_enabled_6, tapo_signal_words, tapo_and_signal_words, tapo_section_name, strahler_1, strahler_2, strahler_3, strahler_4,
                                            plug_1, plug_2, plug_3, plug_4, strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                                            strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color, anschalten_strahler_1_3_color,
                                            anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht, anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                                            anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4, ausschalten_plug,
                                            startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                                            color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait, engine, vosk_recognizer):
    if debug_mode == True: print("Kombination")
    if debug_mode == True: print(pyttsx_voice_id)
    user_combination_inputs =[user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
                         user_combination_input_7, user_combination_input_8, user_combination_input_9, user_combination_input_10]
    # Lese die INI-Datei
    config = configparser.ConfigParser()




    if pyttsx_voice_id == 0:
        if debug_mode == True:print("Deutsche Dateien geladen")
        additional_config_paths = [
            resource_path('config/German_app_config.ini'),
            resource_path('config/German_tapo_config.ini'),
            resource_path('config/German_chat_config.ini'),
            resource_path('config/German_combination_config.ini')            
        ]
        config.read(additional_config_paths)
            
    if pyttsx_voice_id == 2:
        if debug_mode == True:print("Englische Dateien geladen")
        additional_config_paths = [            
            resource_path('config/English_app_config.ini'),
            resource_path('config/English_tapo_config.ini'),
            resource_path('config/English_chat_config.ini'),
            resource_path('config/English_combination_config.ini')
            ]    
        config.read(additional_config_paths)
        
    if pyttsx_voice_id == 4:                        
        if debug_mode == True:print("Spanische Dateien geladen")
        additional_config_paths = [            
            resource_path('config/Spanish_app_config.ini'),
            resource_path('config/Spanish_tapo_config.ini'),
            resource_path('config/Spanish_chat_config.ini'),
            resource_path('config/Spanish_combination_config.ini'),
            # Füge hier die Pfade für die restlichen Config-Dateien hinzu
        ]
        config.read(additional_config_paths)
                        
    
    for user_combination_input in user_combination_inputs:        
        
        if user_combination_input:          
            for i in range(1, 16):
                

                    if pyttsx_voice_id == 0:
                        if debug_mode == True:print("German Settings")
                        # German
                        # ChatSettings Conf
                        section_name = f'ChatSettings Funktion {i}'                        
                        active_chat_engine = config.get(section_name, 'active_chat_engine')                        
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        mouse_click_on_coordinates_1 = config.get(app_section_name, 'mouse_click_on_coordinates_1')
                        double_mouse_click_on_coordinates_1 = config.get(app_section_name, 'double_mouse_click_on_coordinates_1')
                        mouse_click_on_coordinates_2 = config.get(app_section_name, 'mouse_click_on_coordinates_2')
                        double_mouse_click_on_coordinates_2 = config.get(app_section_name, 'double_mouse_click_on_coordinates_2')
                        mouse_click_on_coordinates_3 = config.get(app_section_name, 'mouse_click_on_coordinates_3')
                        double_mouse_click_on_coordinates_3 = config.get(app_section_name, 'double_mouse_click_on_coordinates_3')
                        mouse_click_on_coordinates_4 = config.get(app_section_name, 'mouse_click_on_coordinates_4')
                        double_mouse_click_on_coordinates_4 = config.get(app_section_name, 'double_mouse_click_on_coordinates_4')
                        mouse_click_on_coordinates_5 = config.get(app_section_name, 'mouse_click_on_coordinates_5')
                        double_mouse_click_on_coordinates_5 = config.get(app_section_name, 'double_mouse_click_on_coordinates_5')
                        mouse_click_on_coordinates_6 = config.get(app_section_name, 'mouse_click_on_coordinates_6')
                        double_mouse_click_on_coordinates_6 = config.get(app_section_name, 'double_mouse_click_on_coordinates_6')                        
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'tapo_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'tapo_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')

                        
                    elif pyttsx_voice_id == 2: 
                        if debug_mode == True:print("English Settings") 
                        # English
                        # ChatSettings Conf
                        section_name = f'English_ChatSettings Funktion {i}'
                        active_chat_engine = config.get(section_name, 'active_chat_engine')
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'English_AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'English_TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'tapo_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'tapo_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'English_CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')
                        
                        
                    elif pyttsx_voice_id == 4:
                        if debug_mode == True:print("Spanish Settings")
                        # Spanish
                        # ChatSettings Conf
                        section_name = f'Spanish_ChatSettings Funktion {i}'
                        active_chat_engine = config.get(section_name, 'active_chat_engine')                        
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'Spanish_AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'Spanish_TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'tapo_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'tapo_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'Spanish_CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')
                            
                    if user_input_enabled:
                        user_input_i = user_input + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    else:
                        user_input_i = user_input_task + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                        user_input = user_combination_input

                    if contains_signal_word(user_input, signal_words, and_signal_words, section_name):
                        
                                               
                        if debug_mode == False:clear_voice_assistent()
                        Signal_word_found = True
                        if dialog_chat_enabled:
                            if debug_mode ==False:
                                print_center_zeile("Dialogmodus wird gestartet. Einen kleinen Augenblick bitte.", 1, "left")
                            huggingface_newchat(chatbot)
                            while True:
                                print(user_input_i)
                                if debug_mode ==False: 
                                    print_center_zeile("Dialogmodus                                                                         ", 1, "left")
                                if debug_mode == True: 
                                    print("Dialogmodus")
                                process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id)
                                if debug_mode == True: print("process_user_input fertiggestellt")
                                if debug_mode == True: print("Erster user_input_i: " + user_input_i)
                                user_input_i = get_user_input(vosk_recognizer)
                                if debug_mode == True: print("Folgender user_input_i: " + user_input_i)
                                if "abbruch" in user_input_i.lower() or "stopp" in user_input_i.lower() or "es reicht" in user_input_i.lower() or "stop" in user_input_i.lower() or "parar" in user_input_i.lower():
                                    if pyttsx_voice_id == 0:
                                        text_to_speech(engine, pyttsx_voice_id, "Danke, war ein gutes Gespräch")
                                    elif pyttsx_voice_id == 2:
                                        text_to_speech(engine, pyttsx_voice_id, "Ok, thank you for the nice conversation")
                                    elif pyttsx_voice_id == 4:
                                        text_to_speech(engine, pyttsx_voice_id, "Sie claro, gracias por la buen conversación")
                                    if debug_mode == False:clear_voice_assistent()                              
                                    break
                        else:                                                                                
                            process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id)
                            break

                    elif app_contains_signal_word(user_input, app_signal_words, app_and_signal_words, app_section_name):
                        Signal_word_found = True
                        if debug_mode == True: print("App Funktion")
                        user_input_app = input_app(user_input, app_signal_words, app_and_signal_words)
                        if debug_mode == True:print(user_input_app)
                        
                        if debug_mode == False:clear_voice_assistent()
                        app_ultimate(app, [mouse_click_on_coordinates_1, mouse_click_on_coordinates_2, mouse_click_on_coordinates_3, 
                                               mouse_click_on_coordinates_4, mouse_click_on_coordinates_5, mouse_click_on_coordinates_6], 
                                               [double_mouse_click_on_coordinates_1, double_mouse_click_on_coordinates_2,
                                               double_mouse_click_on_coordinates_3, double_mouse_click_on_coordinates_4, 
                                               double_mouse_click_on_coordinates_5, double_mouse_click_on_coordinates_6],
                                    [hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup],
                                    [wait_app, wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, wait_3_1, wait_3_2, wait_3_3,
                                    wait_4_1, wait_4_2, wait_4_3, wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3],
                                    [text_1, text_2, text_3, text_4, text_5, text_6],
                                    [keys_1_list, keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list],
                                    [user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                    user_input_enabled_4, user_input_enabled_5, user_input_enabled_6],
                                    user_input_app, engine)                      
                        break
                        
                    elif tapo_contains_signal_word(user_input, tapo_signal_words, tapo_and_signal_words, tapo_section_name):
                        Signal_word_found = True
                        Tapo.anmelden(strahler_1, strahler_2, strahler_3, strahler_4)
                        
                        threading.Thread(target=ultimate_light, daemon=True, args=(
                        strahler_1, strahler_2, strahler_3, strahler_4, plug_1, plug_2, plug_3, plug_4,
                        strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                        strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color,
                        anschalten_strahler_1_3_color,
                        anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht,
                        anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                        anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4,
                        ausschalten_plug,
                        startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3,
                        brightness_d3, startfarbe_d4, brightness_d4,
                        color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung,
                        temp, wait)).start()                        
                        break


        else:            
            break        

            
    



#Combinations Ende

#Die Funktion entfernt Umlaute ÜÖÄ aus dem user_input, schaut ob Signal Wörter vorhanden sind und achtet auf die logische Verbindung zwischen den Wörtern or und and
from unidecode import unidecode

def combination_contains_signal_word(user_input, combination_signal_words, combination_and_signal_words):
    try:
        normalized_input = unidecode(user_input.lower())
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Signal_W: " + combination_signal_words)
        if debug_mode == True: print("and_Signal_W: " + combination_and_signal_words)

        # Split the logical OR conditions into individual words
        combination_signal_words = combination_signal_words.split() if combination_signal_words else []
        combination_and_signal_words = combination_and_signal_words.split() if combination_and_signal_words else []

        # Überprüfen der 'or'-Bedingung
        or_bedingung_erfuellt = any(word in normalized_input for word in combination_signal_words)
        if debug_mode == True: print("or_bedingung_erfuellt: ")
        if debug_mode == True: print(or_bedingung_erfuellt)

        # Überprüfen der 'and'-Bedingung
        if len(combination_and_signal_words) > 0:
            and_bedingung_erfuellt = any(word in normalized_input for word in combination_and_signal_words)
        else:
            and_bedingung_erfuellt = True  # 'and'-Bedingung ist erfüllt, wenn keine Wörter angegeben sind
        if debug_mode == True: print("and_bedingung_erfuellt: ")
        if debug_mode == True: print(and_bedingung_erfuellt)

        if or_bedingung_erfuellt and and_bedingung_erfuellt:
            return True
        else:
            return False
    except Exception as e:
            if debug_mode == True: print("combination_contains_signal_word")
            if debug_mode == True: print(f"Error: {e}")

def tapo_contains_signal_word(user_input, tapo_signal_words, tapo_and_signal_words, tapo_section_name):
    try:
        normalized_input = unidecode(user_input.lower())
        if debug_mode == True: print("")
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Funktionsnamen: " + tapo_section_name)
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("Signal_W: " + tapo_signal_words)
        if debug_mode == True: print("and_Signal_W: " + tapo_and_signal_words)
        if debug_mode == True: print("")
        

        # Split the logical OR conditions into individual words
        tapo_signal_words = tapo_signal_words.split() if tapo_signal_words else []
        tapo_and_signal_words = tapo_and_signal_words.split() if tapo_and_signal_words else []

        # Überprüfen der 'or'-Bedingung
        or_bedingung_erfuellt = any(word in normalized_input for word in tapo_signal_words)
        if debug_mode == True: print("")
        if debug_mode == True: print("or_bedingung_erfuellt: ")
        if debug_mode == True: print(or_bedingung_erfuellt)

        # Überprüfen der 'and'-Bedingung
        if len(tapo_and_signal_words) > 0:
            and_bedingung_erfuellt = any(word in normalized_input for word in tapo_and_signal_words)
        else:
            and_bedingung_erfuellt = True  # 'and'-Bedingung ist erfüllt, wenn keine Wörter angegeben sind
        if debug_mode == True: print("and_bedingung_erfuellt: ")
        if debug_mode == True: print(and_bedingung_erfuellt)
        if debug_mode == True: print("------------------------------------------")

        if or_bedingung_erfuellt and and_bedingung_erfuellt:
            return True
        else:
            return False
    except Exception as e:
            if debug_mode == True: print("tapo_contains_signal_word: ")
            if debug_mode == True: print(f"Error: {e}")
            if debug_mode == True: print("-------------------------------------------")
            if debug_mode == True: print("")

def app_contains_signal_word(user_input, app_signal_words, app_and_signal_words, app_section_name):
    try:
        normalized_input = unidecode(user_input.lower())
        if debug_mode == True: print("")
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Funktionsnamen: " + app_section_name)
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("Signal_W: " + app_signal_words)
        if debug_mode == True: print("and_Signal_W: " + app_and_signal_words)
        if debug_mode == True: print("")

        # Split the logical OR conditions into individual words
        app_signal_words = app_signal_words.split() if app_signal_words else []
        app_and_signal_words = app_and_signal_words.split() if app_and_signal_words else []

        # Überprüfen der 'or'-Bedingung
        or_bedingung_erfuellt = any(word in normalized_input for word in app_signal_words)
        if debug_mode == True: print("")
        if debug_mode == True: print("or_bedingung_erfuellt: ")
        if debug_mode == True: print(or_bedingung_erfuellt)
        

        # Überprüfen der 'and'-Bedingung
        if len(app_and_signal_words) > 0:
            and_bedingung_erfuellt = any(word in normalized_input for word in app_and_signal_words)
        else:
            and_bedingung_erfuellt = True  # 'and'-Bedingung ist erfüllt, wenn keine Wörter angegeben sind
        if debug_mode == True: print("and_bedingung_erfuellt: ")
        if debug_mode == True: print(and_bedingung_erfuellt)
        if debug_mode == True: print("------------------------------------------")

        if or_bedingung_erfuellt and and_bedingung_erfuellt:
            return True
        else:
            return False
    except Exception as e:
            if debug_mode == True: print("app_contains_signal_word")
            if debug_mode == True: print(f"Error: {e}")
            if debug_mode == True: print("-------------------------------------------")
            if debug_mode == True: print("")

def contains_signal_word(user_input, signal_words, and_signal_words, section_name):
    if debug_mode == True: print("contains_signal_word")
    try:
        normalized_input = unidecode(user_input.lower()) 
        if debug_mode == True: print("")
        if debug_mode == True: print("-------------------------------------------")       
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Funktionsnamen: " + section_name)        
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("Signal_W: " + signal_words)
        if debug_mode == True: print("and_Signal_W: " + and_signal_words)
        if debug_mode == True: print("")

        # Split the logical OR conditions into individual words
        signal_words = signal_words.split() if signal_words else []
        and_signal_words = and_signal_words.split() if and_signal_words else []

        # Überprüfen der 'or'-Bedingung
        or_bedingung_erfuellt = any(word in normalized_input for word in signal_words)
        if debug_mode == True: print("")
        if debug_mode == True: print("or_bedingung_erfuellt: ")
        if debug_mode == True: print(or_bedingung_erfuellt)

        # Überprüfen der 'and'-Bedingung
        if len(and_signal_words) > 0:
            and_bedingung_erfuellt = any(word in normalized_input for word in and_signal_words)
        else:
            and_bedingung_erfuellt = True  # 'and'-Bedingung ist erfüllt, wenn keine Wörter angegeben sind
        if debug_mode == True: print("and_bedingung_erfuellt: ")
        if debug_mode == True: print(and_bedingung_erfuellt)
        if debug_mode == True: print("-------------------------------------------")

        if or_bedingung_erfuellt and and_bedingung_erfuellt:
            return True
        else:
            return False
    except Exception as e:
            if debug_mode == True: print("contains_signal_word")
            if debug_mode == True: print(f"Error: {e}")
            if debug_mode == True: print("-------------------------------------------")
            if debug_mode == True: print("")

def contains_change_user_or_language(user_input, change_language, change_user, section_name):
    
    if debug_mode == True: print("contains_change_user_language")
    try:
        normalized_input = unidecode(user_input.lower()) 
        if debug_mode == True: print("")
        if debug_mode == True: print("-------------------------------------------")       
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Funktionsnamen: " + section_name)        
        if debug_mode == True: print("-------------------------------------------")
        if debug_mode == True: print("change_language_wort: " + change_language)
        if debug_mode == True: print("change_user_wort: " + change_user)
        if debug_mode == True: print("")

        # Split the logical OR conditions into individual words
        change_user = change_user.split() if change_user else []
        change_language = change_language.split() if change_language else []

        # Überprüfen der User 'or'-Bedingung
        user_or_bedingung_erfuellt = any(word in normalized_input for word in change_user)
        if debug_mode == True: print("")
        if debug_mode == True: print("user_or_bedingung_erfuellt: ")
        if debug_mode == True: print(user_or_bedingung_erfuellt)
        # Überprüfen der User 'or'-Bedingung
        language_or_bedingung_erfuellt = any(word in normalized_input for word in change_language)
        if debug_mode == True: print("language_or_bedingung_erfuellt: ")
        if debug_mode == True: print(language_or_bedingung_erfuellt)
        if debug_mode == True: print("-------------------------------------------")
        
        if user_or_bedingung_erfuellt == True and language_or_bedingung_erfuellt == True:
            return False
        elif user_or_bedingung_erfuellt == True: 
            change_user = "change_user"
            return change_user
        elif language_or_bedingung_erfuellt == True:
            change_language = "change_language"
            return change_language
        else:
            return False
    except Exception as e:
            if debug_mode == True: print("contains_change_user_or_language")
            if debug_mode == True: print(f"Error: {e}")
            if debug_mode == True: print("-------------------------------------------")
            if debug_mode == True: print("")





def change_user_or_language(contains_change_user_or_language):
    if debug_mode == True: print("change_user_or_language")
    if debug_mode == True: print("contains_change_user_or_language: " + str(contains_change_user_or_language))
    
    if contains_change_user_or_language.lower() == "change_user":
        current_state = states['BENUTZER']

    if contains_change_user_or_language.lower() == "change_language":
        current_state = states['ASK_LANG']

    if contains_change_user_or_language == False:
        current_state = states['ASK_TOPIC']
    return current_state


def contains_benutzername(benutzername_erfragt, benutzername):
    try:
        normalized_input = unidecode(benutzername_erfragt.lower())
        if debug_mode == True: print("normalized_input: " + normalized_input)
        if debug_mode == True: print("Benutzername: " + benutzername)


        if benutzername_erfragt:
            if benutzername_erfragt == benutzername:
                if debug_mode == True: print("Benutzername erkannt: ")
                if debug_mode == True: print(benutzername)
                return True
            else:
                if debug_mode == True: print("Benutzername nicht erkannt")
                return False
        
    except Exception as e:
            if debug_mode == True: print("contains_benutzername")
            if debug_mode == True: print(f"Error: {e}")



    
    

def vosk_sprache(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch):
    
    try:
        if vosk_sprache_deutsch == True:
            model = Model(resource_path(r"zubehoer/vosk-model-small-de-zamia-0.3"))
            if debug_mode == True: print(model)
                  
        elif vosk_sprache_englisch == True:
            model = Model(resource_path(r"zubehoer/vosk-model-small-en-us-0.15"))
            if debug_mode == True: print(model)
                         
        elif vosk_sprache_spanisch == True:
            model = Model(resource_path(r"zubehoer/vosk-model-small-es-0.42"))
            if debug_mode == True: print(model)
        
        vosk_recognizer = KaldiRecognizer(model, 32000)        
    except Exception as e:            
            if debug_mode == True: print("vosk_sprache: " + f"Error: {e}")
    return vosk_recognizer

def pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch):
    global pyttsx_voice_id
    try:
        if vosk_sprache_deutsch == True:
            
            voice = 0
                
        elif vosk_sprache_englisch == True:
            
            voice = 2
                         
        elif vosk_sprache_spanisch == True:
            
            voice = 4
        
        pyttsx_voice_id = voice
    except Exception as e:            
            if debug_mode == True: print("vosk_sprache: " + f"Error: {e}")
    return pyttsx_voice_id

import shutil


states = {
    'BENUTZER': 0,
    'ASK_TOPIC': 1,
    'ASK_LANG': 2,
    'TRANSLATE': 3,
    'FORMULATE_TEXT': 4,
    'ASSISTANT': 5,
    'TALKALONG': 6,
}
# Initialize state
current_state = states['ASK_LANG']
previous_state = states['ASK_LANG']

marker_satz_3 = 'Ask_Topic_espanol:'
random_satz_3 = get_random_sentence_from_file(file_path_satz, marker_satz_3)
marker_satz_4 = 'Ask_Topic_Again_espanol:'
random_satz_4 = get_random_sentence_from_file(file_path_satz, marker_satz_4)
marker_satz_5 = 'Ask_Topic:'
random_satz_5 = get_random_sentence_from_file(file_path_satz, marker_satz_5)
marker_satz_6 = 'Ask_Topic_Again:'
random_satz_6 = get_random_sentence_from_file(file_path_satz, marker_satz_6)
marker_satz_7 = 'Ask_Topic_englisch:'
random_satz_7 = get_random_sentence_from_file(file_path_satz, marker_satz_7)
marker_satz_8 = 'Ask_Topic_Again_englisch:'
random_satz_8 = get_random_sentence_from_file(file_path_satz, marker_satz_8)


def unterschied_sprache_random_satz(random_satz_3, random_satz_4, random_satz_5, random_satz_6, random_satz_7, random_satz_8, pyttsx_voice_id):     
    if debug_mode == True: print(pyttsx_voice_id)
    if debug_mode == True: print(random_satz_3)
    if debug_mode == True: print(random_satz_4)
    if debug_mode == True: print(random_satz_5)
    if debug_mode == True: print(random_satz_6)
    if debug_mode == True: print(random_satz_7)
    if debug_mode == True: print(random_satz_8)

    if pyttsx_voice_id == 0:
        random_satz_1 = random_satz_3
        random_satz_2 = random_satz_4
    elif pyttsx_voice_id == 4:
        random_satz_1 = random_satz_5
        random_satz_2 = random_satz_6
    elif pyttsx_voice_id == 2:
        random_satz_1 = random_satz_7
        random_satz_2 = random_satz_8
    if debug_mode == True: print(random_satz_1 + random_satz_2)
    return random_satz_1, random_satz_2

def unterschied_sprache_ein_random_satz(german_satz, english_satz, spanisch_satz, pyttsx_voice_id):     
    if debug_mode == True: print(pyttsx_voice_id)
    if debug_mode == True: print(german_satz)
    if debug_mode == True: print(english_satz)
    if debug_mode == True: print(spanisch_satz)
    
    if pyttsx_voice_id == 0:
        random_satz_1 = german_satz
        
    elif pyttsx_voice_id == 2:
        random_satz_1 = english_satz
        
    elif pyttsx_voice_id == 4:
        random_satz_1 = spanisch_satz
        r
    if debug_mode == True: print(random_satz_1)
    return random_satz_1

"""""
def chat_dialog(engine):#, App_instance):
    global current_state, previous_state, chatbot, Signal_word_found, vosk_recognizer, pyttsx_voice_id, debug_mode
    current_state = states['BENUTZER']
    previous_state = states['BENUTZER'] 
    
    
    

    # Lese die INI-Datei
    config = configparser.ConfigParser()

    # Füge die Standard-Config hinzu
    config.read(resource_path('config/benutzer_settings_config.ini'))   
    
    
    while True:
        
        try:
            if current_state == states['ASK_LANG']:
                model = Model(resource_path(r"zubehoer/vosk-model-small-en-us-0.15"))
                vosk_recognizer = KaldiRecognizer(model, 32000)   
                pyttsx_voice_id = 2
                if debug_mode == False:clear_voice_assistent()                   
                user_input = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Do you prefer German, English or Spanish for your Session?")                          
                
                if user_input:
                    if user_input.lower() == "deutsch" or user_input.lower() == "german" or user_input.lower() == "aleman":
                        vosk_sprache_deutsch = True
                        vosk_sprache_englisch = False
                        vosk_sprache_spanisch = False
                        pyttsx_voice_id = 0
                        if debug_mode == True:print("Deutsche Dateien geladen")
                        additional_config_paths = [
                            resource_path('config/German_app_config.ini'),
                            resource_path('config/German_tapo_config.ini'),
                            resource_path('config/German_chat_config.ini'),
                            resource_path('config/German_combination_config.ini')            
                        ]
                        config.read(additional_config_paths)
                        vosk_recognizer = vosk_sprache(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        if debug_mode == False:clear_voice_assistent()
                        current_state = states['ASK_TOPIC']
                    elif user_input.lower() == "englisch" or user_input.lower() == "english" or user_input.lower() == "ingles":
                        vosk_sprache_deutsch = False
                        vosk_sprache_englisch = True
                        vosk_sprache_spanisch = False
                        pyttsx_voice_id = 2
                        if debug_mode == True:print("Englische Dateien geladen")
                        additional_config_paths = [            
                            resource_path('config/English_app_config.ini'),
                            resource_path('config/English_tapo_config.ini'),
                            resource_path('config/English_chat_config.ini'),
                            resource_path('config/English_combination_config.ini')
                            ]    
                        config.read(additional_config_paths)
                        vosk_recognizer = vosk_sprache(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        pyttsx_voice_id = pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        if debug_mode == False:clear_voice_assistent()
                        current_state = states['ASK_TOPIC']
                    elif user_input.lower() == "spanisch" or user_input.lower() == "spanish" or user_input.lower() == "espanol":
                        vosk_sprache_deutsch = False
                        vosk_sprache_englisch = False
                        vosk_sprache_spanisch = True
                        pyttsx_voice_id = 4
                        if debug_mode == True:print("Spanische Dateien geladen")
                        additional_config_paths = [            
                            resource_path('config/Spanish_app_config.ini'),
                            resource_path('config/Spanish_tapo_config.ini'),
                            resource_path('config/Spanish_chat_config.ini'),
                            resource_path('config/Spanish_combination_config.ini'),
                            # Füge hier die Pfade für die restlichen Config-Dateien hinzu
                        ]
                        config.read(additional_config_paths)
                        vosk_recognizer = vosk_sprache(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        pyttsx_voice_id = pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        if debug_mode == False:clear_voice_assistent()
                        current_state = states['ASK_TOPIC']
                    else:
                        text_to_speech(engine, pyttsx_voice_id, "Please chose an existing Language we do not offer " + user_input)
                        current_state = states['ASK_LANG']
                        continue
                if not user_input:
                    text_to_speech(engine, pyttsx_voice_id, "Please chose a Language")
                    current_state = states['ASK_LANG']
                    continue
                

                    

                


            if current_state == states['BENUTZER']: 
                model = Model(resource_path(r"zubehoer/vosk-model-small-en-us-0.15"))
                vosk_recognizer = KaldiRecognizer(model, 32000)   
                pyttsx_voice_id = 2
                if debug_mode == False:clear_voice_assistent()            
                user_input = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Whats your Username?")                
                benutzername_erfragt = user_input
                user_found = False  # Flag to check if a user is found
                
                for i in range(1, 16):
                    # Benutzer_settings_config
                    benutzer_section_name = f'Benutzer_{i}_config'
                    if debug_mode == True: print(benutzer_section_name)
                    benutzername = config.get(benutzer_section_name, 'benutzername')
                    tapo_e_mail = config.get(benutzer_section_name, 'tapo_e_mail')
                    if debug_mode == True: print(tapo_e_mail)
                    tapo_passwort = config.get(benutzer_section_name, 'tapo_passwort')
                    tapo_s_ip_1 = config.get(benutzer_section_name, 'tapo_s_ip_1')
                    tapo_s_ip_2 = config.get(benutzer_section_name, 'tapo_s_ip_2')
                    tapo_s_ip_3 = config.get(benutzer_section_name, 'tapo_s_ip_3')
                    tapo_s_ip_4 = config.get(benutzer_section_name, 'tapo_s_ip_4')
                    tapo_p_ip_1 = config.get(benutzer_section_name, 'tapo_p_ip_1')
                    tapo_p_ip_2 = config.get(benutzer_section_name, 'tapo_p_ip_2')
                    tapo_p_ip_3 = config.get(benutzer_section_name, 'tapo_p_ip_3')
                    tapo_p_ip_4 = config.get(benutzer_section_name, 'tapo_p_ip_4')
                    vosk_sprache_deutsch = config.getboolean(benutzer_section_name, 'vosk_sprache_deutsch')
                    vosk_sprache_englisch = config.getboolean(benutzer_section_name, 'vosk_sprache_englisch')
                    vosk_sprache_spanisch = config.getboolean(benutzer_section_name, 'vosk_sprache_spanisch')
                    if debug_mode == True:print("1")
                    if debug_mode == True:print(vosk_sprache_deutsch)
                    if debug_mode == True:print("2")
                    if debug_mode == True:print(vosk_sprache_englisch)
                    if debug_mode == True:print("3")
                    if debug_mode == True:print(vosk_sprache_spanisch)
                    
                    
                    

                    if contains_benutzername(benutzername_erfragt, benutzername):                        
                        text_to_speech(engine, pyttsx_voice_id, benutzername)
                        if debug_mode == True: print(tapo_e_mail)
                        current_state = states['ASK_LANG']
                        user_found = True  # Set the flag to True if a user is found                         
                        break

                    

                if not user_found:
                    text_to_speech(engine, pyttsx_voice_id, benutzername_erfragt + " ist kein registrierter Benutzer.")
                    current_state = states['BENUTZER']
                    if debug_mode == True: print("keine übereinstimmung")                                         

            strahler_1 = PyL530.L530(tapo_s_ip_1, tapo_e_mail, tapo_passwort)
            strahler_2 = PyL530.L530(tapo_s_ip_2, tapo_e_mail, tapo_passwort)
            strahler_3 = PyL530.L530(tapo_s_ip_3, tapo_e_mail, tapo_passwort)
            strahler_4 = PyL530.L530(tapo_s_ip_4, tapo_e_mail, tapo_passwort)

            plug_1 = PyP100.P100(tapo_p_ip_1, tapo_e_mail, tapo_passwort)
            plug_2 = PyP100.P100(tapo_p_ip_2, tapo_e_mail, tapo_passwort)
            plug_3 = PyP100.P100(tapo_p_ip_3, tapo_e_mail, tapo_passwort)
            plug_4 = PyP100.P100(tapo_p_ip_4, tapo_e_mail, tapo_passwort)

            if current_state == states['ASK_TOPIC']:
                vosk_recognizer = vosk_sprache(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                pyttsx_voice_id = pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                if debug_mode == False:clear_voice_assistent()
                if debug_mode == True:print(pyttsx_voice_id)
                random_satz_1, random_satz_2 = unterschied_sprache_random_satz(random_satz_5, random_satz_6, random_satz_3, random_satz_4, random_satz_7, random_satz_8, pyttsx_voice_id)
                
                if debug_mode == True: print("random Satz: " + random_satz_1 + random_satz_2)
                current_ask_topic_sentence = random_satz_1                
                user_input = text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, {current_ask_topic_sentence})
                if debug_mode == True: print("Sections:", config.sections())
                Signal_word_found = False  # Flag to check if a user is found

                for i in range(1, 16):
                    if pyttsx_voice_id == 0:
                        if debug_mode == True:print("German Settings")
                        # German
                        # ChatSettings Conf
                        section_name = f'ChatSettings Funktion {i}'
                        active_chat_engine = config.get(section_name, 'active_chat_engine')
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'licht_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'licht_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')
                        

                    if pyttsx_voice_id == 2: 
                        if debug_mode == True:print("English Settings")  
                        # English
                        # ChatSettings Conf
                        section_name = f'English_ChatSettings Funktion {i}'
                        active_chat_engine = config.get(section_name, 'active_chat_engine')
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'English_AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'English_TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'licht_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'licht_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'English_CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')
                        
                        
                    if pyttsx_voice_id == 4:
                        if debug_mode == True:print("Spanish Settings")
                        # Spanish
                        # ChatSettings Conf
                        section_name = f'Spanish_ChatSettings Funktion {i}'
                        active_chat_engine = config.get(section_name, 'active_chat_engine')
                        signal_words = config.get(section_name, 'signal_words')
                        and_signal_words = config.get(section_name, 'and_signal_words')
                        user_input_task = config.get(section_name, 'user_input_task')
                        user_input_context = config.get(section_name, 'user_input_context')
                        user_input_example = config.get(section_name, 'user_input_example')
                        user_input_persona = config.get(section_name, 'user_input_persona')
                        user_input_format = config.get(section_name, 'user_input_format')
                        user_input_tone = config.get(section_name, 'user_input_tone')
                        user_input_enabled = config.getboolean(section_name, 'user_input_enabled')
                        dialog_chat_enabled = config.getboolean(section_name, 'dialog_chat_enabled')
                        # AppSettings Config
                        app_section_name = f'Spanish_AppSettings Funktion {i}'
                        app = config.get(app_section_name, 'app')
                        app_signal_words = config.get(app_section_name, 'app_signal_words')
                        app_and_signal_words = config.get(app_section_name, 'app_and_signal_words')
                        hotkey_1_str = config.get(app_section_name, 'hotkey_1')
                        hotkey_1_tup = tuple(hotkey_1_str.split(','))
                        hotkey_2_str = config.get(app_section_name, 'hotkey_2')
                        hotkey_2_tup = tuple(hotkey_2_str.split(','))
                        hotkey_3_str = config.get(app_section_name, 'hotkey_3')
                        hotkey_3_tup = tuple(hotkey_3_str.split(','))
                        hotkey_4_str = config.get(app_section_name, 'hotkey_4')
                        hotkey_4_tup = tuple(hotkey_4_str.split(','))
                        hotkey_5_str = config.get(app_section_name, 'hotkey_5')
                        hotkey_5_tup = tuple(hotkey_5_str.split(','))
                        hotkey_6_str = config.get(app_section_name, 'hotkey_6')
                        hotkey_6_tup = tuple(hotkey_6_str.split(','))
                        wait_app = config.getfloat(app_section_name, 'wait_app')
                        wait_1_1 = config.getfloat(app_section_name, 'wait_1_1')
                        wait_1_2 = config.getfloat(app_section_name, 'wait_1_2')
                        wait_1_3 = config.getfloat(app_section_name, 'wait_1_3')
                        wait_2_1 = config.getfloat(app_section_name, 'wait_2_1')
                        wait_2_2 = config.getfloat(app_section_name, 'wait_2_2')
                        wait_2_3 = config.getfloat(app_section_name, 'wait_2_3')
                        wait_3_1 = config.getfloat(app_section_name, 'wait_3_1')
                        wait_3_2 = config.getfloat(app_section_name, 'wait_3_2')
                        wait_3_3 = config.getfloat(app_section_name, 'wait_3_3')
                        wait_4_1 = config.getfloat(app_section_name, 'wait_4_1')
                        wait_4_2 = config.getfloat(app_section_name, 'wait_4_2')
                        wait_4_3 = config.getfloat(app_section_name, 'wait_4_3')
                        wait_5_1 = config.getfloat(app_section_name, 'wait_5_1')
                        wait_5_2 = config.getfloat(app_section_name, 'wait_5_2')
                        wait_5_3 = config.getfloat(app_section_name, 'wait_5_3')
                        wait_6_1 = config.getfloat(app_section_name, 'wait_6_1')
                        wait_6_2 = config.getfloat(app_section_name, 'wait_6_2')
                        wait_6_3 = config.getfloat(app_section_name, 'wait_6_3')
                        text_1 = config.get(app_section_name, 'Text_1')
                        text_2 = config.get(app_section_name, 'Text_2')
                        text_3 = config.get(app_section_name, 'Text_3')
                        text_4 = config.get(app_section_name, 'Text_4')
                        text_5 = config.get(app_section_name, 'Text_5')
                        text_6 = config.get(app_section_name, 'Text_6')
                        keys_1_str = config.get(app_section_name, 'Keys_1')
                        keys_1_list = ast.literal_eval(f"[{keys_1_str}]")
                        keys_2_str = config.get(app_section_name, 'keys_2')
                        keys_2_list = ast.literal_eval(f"[{keys_2_str}]")
                        keys_3_str = config.get(app_section_name, 'keys_3')
                        keys_3_list = ast.literal_eval(f"[{keys_3_str}]")
                        keys_4_str = config.get(app_section_name, 'keys_4')
                        keys_4_list = ast.literal_eval(f"[{keys_4_str}]")
                        keys_5_str = config.get(app_section_name, 'keys_5')
                        keys_5_list = ast.literal_eval(f"[{keys_5_str}]")
                        keys_6_str = config.get(app_section_name, 'keys_6')
                        keys_6_list = ast.literal_eval(f"[{keys_6_str}]")
                        user_input_enabled_1 = config.getboolean(app_section_name, 'user_input_1')
                        user_input_enabled_2 = config.getboolean(app_section_name, 'user_input_2')
                        user_input_enabled_3 = config.getboolean(app_section_name, 'user_input_3')
                        user_input_enabled_4 = config.getboolean(app_section_name, 'user_input_4')
                        user_input_enabled_5 = config.getboolean(app_section_name, 'user_input_5')
                        user_input_enabled_6 = config.getboolean(app_section_name, 'user_input_6')
                        # Lichtfunktionen
                        tapo_section_name = f'Spanish_TapoSettings_Funktion_{i}'
                        tapo_signal_words = config.get(tapo_section_name, 'licht_signal_word')
                        tapo_and_signal_words = config.get(tapo_section_name, 'licht_and_signal_word')
                        # Effekte und Funktionen für Strahler
                        strahler_color_strobe_multi = config.getboolean(tapo_section_name,
                                                                        'strahler_color_strobe_multi')
                        strahler_color_fade_multi = config.getboolean(tapo_section_name,
                                                                    'strahler_color_fade_multi')
                        strahler_slow_fade_out = config.getboolean(tapo_section_name, 'strahler_slow_fade_out')
                        strahler_speed_fade_out = config.getboolean(tapo_section_name, 'strahler_speed_fade_out')
                        anschalten_strahler_multi_color = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_color')
                        anschalten_strahler_2_4_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_color')
                        anschalten_strahler_1_3_color = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_color')
                        anschalten_strahler_multi_licht = config.getboolean(tapo_section_name,
                                                                            'anschalten_strahler_multi_licht')
                        anschalten_strahler_2_4_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_2_4_licht')
                        anschalten_strahler_1_3_licht = config.getboolean(tapo_section_name,
                                                                        'anschalten_strahler_1_3_licht')
                        ausschalten_strahler = config.getboolean(tapo_section_name, 'ausschalten_strahler')
                        # Funktionen für Plug´s
                        anschalten_plug_multi = config.getboolean(tapo_section_name, 'anschalten_plug_multi')
                        anschalten_plug_2_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_4')
                        anschalten_plug_1_3 = config.getboolean(tapo_section_name, 'anschalten_plug_1_3')
                        anschalten_plug_1 = config.getboolean(tapo_section_name, 'anschalten_plug_1')
                        anschalten_plug_2_3_4 = config.getboolean(tapo_section_name, 'anschalten_plug_2_3_4')
                        ausschalten_plug = config.getboolean(tapo_section_name, 'ausschalten_plug')
                        # Funktion "Anschalten" mit folgenden Werten: brightness und temp für Licht. brightness, farbton und saettigung für color.
                        brightness = config.getint(tapo_section_name, 'brightness')
                        temp = config.getint(tapo_section_name, 'temp')
                        farbton = config.getint(tapo_section_name, 'farbton')
                        saettigung = config.getint(tapo_section_name, 'saettigung')
                        # Funktion "...._fade_out" mit folgenden Werten
                        dimmzielwert = config.getint(tapo_section_name, 'dimmzielwert')
                        dimm_geschwindigkeit = config.getfloat(tapo_section_name, 'dimm_geschwindigkeit')
                        # Funktion "color_...._multi" mit folgenden Werten
                        startfarbe_d1 = config.getint(tapo_section_name, 'startfarbe_d1')
                        startfarbe_d2 = config.getint(tapo_section_name, 'startfarbe_d2')
                        startfarbe_d3 = config.getint(tapo_section_name, 'startfarbe_d3')
                        startfarbe_d4 = config.getint(tapo_section_name, 'startfarbe_d4')
                        brightness_d1 = config.getint(tapo_section_name, 'brightness_d1')
                        brightness_d2 = config.getint(tapo_section_name, 'brightness_d2')
                        brightness_d3 = config.getint(tapo_section_name, 'brightness_d3')
                        brightness_d4 = config.getint(tapo_section_name, 'brightness_d4')
                        wait = config.getfloat(tapo_section_name, 'wait')
                        color_distanz = config.getint(tapo_section_name, 'color_distanz')
                        #Combination Funktionen
                        combination_section_name = f'Spanish_CombinationSettings_Funktion_{i}'
                        combination_signal_words = config.get(combination_section_name, 'combination_signal_words')
                        combination_and_signal_words = config.get(combination_section_name, 'combination_and_signal_words')
                        user_combination_input_1 = config.get(combination_section_name, 'user_combination_input_1')
                        user_combination_input_2 = config.get(combination_section_name, 'user_combination_input_2')
                        user_combination_input_3 = config.get(combination_section_name, 'user_combination_input_3')
                        user_combination_input_4 = config.get(combination_section_name, 'user_combination_input_4')
                        user_combination_input_5 = config.get(combination_section_name, 'user_combination_input_5')
                        user_combination_input_6 = config.get(combination_section_name, 'user_combination_input_6')
                        user_combination_input_7 = config.get(combination_section_name, 'user_combination_input_7')
                        user_combination_input_8 = config.get(combination_section_name, 'user_combination_input_8')
                        user_combination_input_9 = config.get(combination_section_name, 'user_combination_input_9')
                        user_combination_input_10 = config.get(combination_section_name, 'user_combination_input_10')
                        

                    if user_input_enabled:
                        user_input_i = user_input + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    else:
                        user_input_i = user_input_task + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    if user_input.lower() == "benutzer wechsel" or user_input.lower() == "change user" or user_input.lower() == "cambiar usuario":
                        current_state = states['BENUTZER']
                    elif user_input.lower() == "hilfe" or user_input.lower() == "help" or user_input.lower() == "ayudar":
                        count = 0
                        if count < 1:
                            text_to_speech(engine, pyttsx_voice_id, "ok")
                            count += 1
                        if len(signal_words) > 0 or len(and_signal_words) > 0:
                            print(section_name)
                            print("signal_words: " + signal_words)
                            print("and_signal_words: " + and_signal_words)
                            print("----------------------------------------------")
                        if len(app_signal_words) > 0 or len(app_and_signal_words) > 0:
                            print("                                              " + app_section_name)
                            print(
                                "                                              signal_words: " + app_signal_words)
                            print(
                                "                                              and_signal_words: " + app_and_signal_words)
                            print(
                                "                                              ----------------------------------------------")
                        if len(tapo_signal_words) > 0 or len(tapo_and_signal_words) > 0:
                            print(
                                "                                                                                            " + tapo_section_name)
                            print(
                                "                                                                                            signal_words: " + tapo_signal_words)
                            print(
                                "                                                                                            and_signal_words: " + tapo_and_signal_words)
                            print(
                                "                                                                                            ----------------------------------------------")
                    elif user_input.lower() == "sprache ändern" or user_input.lower() == "sprache wechseln" or user_input.lower() == "change language" or user_input.lower() == "cambiar el idioma":
                        current_state = states['ASK_LANG']
                        break

                    elif combination_contains_signal_word(user_input, combination_signal_words, combination_and_signal_words):                        
                        text_to_speech(engine, pyttsx_voice_id, "ok")
                        if debug_mode == False:clear_voice_assistent()
                        Signal_word_found = True
                        ultimate_combination(user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
                                            user_combination_input_7, user_combination_input_8, user_combination_input_9, user_combination_input_10, signal_words, and_signal_words, section_name, dialog_chat_enabled, 
                                            app_signal_words, app_and_signal_words, app_section_name, app, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup, wait_app,
                                            wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                            wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3, text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                            keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list, user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                            user_input_enabled_4, user_input_enabled_5, user_input_enabled_6, tapo_signal_words, tapo_and_signal_words, tapo_section_name, strahler_1, strahler_2, strahler_3, strahler_4,
                                            plug_1, plug_2, plug_3, plug_4, strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                                            strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color, anschalten_strahler_1_3_color,
                                            anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht, anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                                            anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4, ausschalten_plug,
                                            startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                                            color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait)
                        
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']
                        break
                        
                    elif contains_signal_word(user_input, signal_words, and_signal_words, section_name):
                        text_to_speech(engine, pyttsx_voice_id, "ok")
                        if debug_mode == False:clear_voice_assistent()
                        Signal_word_found = True
                        if dialog_chat_enabled:
                            print_center_zeile("Dialogmodus wird gestartet. Einen kleinen Augenblick bitte.", 1, "left")
                            huggingface_newchat(chatbot)
                            while True:
                                print_center_zeile("Dialogmodus                                                                         ", 1, "left")
                                process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id)
                                if debug_mode == True: print("process_user_input fertiggestellt")
                                user_input_i = get_user_input(vosk_recognizer)
                                if debug_mode == True: print("user_input_i: " + user_input_i)
                                if "abbruch" in user_input_i.lower() or "stopp" in user_input_i.lower() or "es reicht" in user_input_i.lower() or "stop" in user_input_i.lower() or "parar" in user_input_i.lower():
                                    if pyttsx_voice_id == 0:
                                        text_to_speech(engine, pyttsx_voice_id, "Danke, war ein gutes Gespräch")
                                    elif pyttsx_voice_id == 2:
                                        text_to_speech(engine, pyttsx_voice_id, "Ok, thank you for the nice conversation")
                                    elif pyttsx_voice_id == 4:
                                        text_to_speech(engine, pyttsx_voice_id, "Sie claro, gracias por la buen conversación")
                                    if debug_mode == False:clear_voice_assistent()                                    
                                    current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                                    previous_state = states['ASK_TOPIC']
                                    break
                        else:                                                                                
                            process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id)
                            current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                            previous_state = states['ASK_TOPIC']
                            break

                    elif app_contains_signal_word(user_input, app_signal_words, app_and_signal_words, app_section_name):
                        text_to_speech(engine, pyttsx_voice_id, "ok")
                        Signal_word_found = True
                        if debug_mode == True: print("App Funktion")
                        user_input_app = input_app(user_input, app_signal_words, app_and_signal_words)
                        if debug_mode == True:print(user_input_app)
                        app_ultimate(app, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup, wait_app,
                                    wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, 
                                    wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                    wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3,
                                    text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                    keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list,
                                    user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                    user_input_enabled_4, user_input_enabled_5, user_input_enabled_6,
                                    user_input_app)
                        previous_state = states['ASK_TOPIC']
                        break
                        
                    elif tapo_contains_signal_word(user_input, tapo_signal_words, tapo_and_signal_words, tapo_section_name):
                        text_to_speech(engine, pyttsx_voice_id, "ok")
                        Signal_word_found = True
                        Tapo.anmelden(strahler_1, strahler_2, strahler_3, strahler_4)
                        
                        threading.Thread(target=ultimate_light, daemon=True, args=(
                        strahler_1, strahler_2, strahler_3, strahler_4, plug_1, plug_2, plug_3, plug_4,
                        strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                        strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color,
                        anschalten_strahler_1_3_color,
                        anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht,
                        anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                        anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4,
                        ausschalten_plug,
                        startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3,
                        brightness_d3, startfarbe_d4, brightness_d4,
                        color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung,
                        temp, wait)).start()
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']

                    
                    else:
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']                        
                        if debug_mode == True: print("No matching signal words found.")
            else:
                if debug_mode == True: print("error No matching signal words found.")

        except Exception as e:
            if debug_mode == True: print("chat_dialog" + f"Error: {e}")
            text_to_speech(engine, pyttsx_voice_id, "unbekannte Wörter oder Problem. Bitte überleg mal woran es liegen könnte.")
            current_state = states['ASK_TOPIC']
            previous_state = states['ASK_TOPIC']  # Reset previous_state in case of an error

# Voice Assistent Logik und Funktionsimplementierungen Ende
if __name__ == "__main__":     
    from vosk import Model, KaldiRecognizer
    import pyttsx3    
    engine = pyttsx3.init()
        
    if debug_mode == False: clear_voice_assistent()
    # Initialize Huggingface chatbot
    chatbot = initialize_huggingface()
    huggingface_newchat(chatbot)     
    if debug_mode == False: clear_voice_assistent()    
    #app = ConsoleApp()
    chat_dialog_thread = threading.Thread(target=chat_dialog(engine))#, daemon=True, args=(engine, app))
    chat_dialog_thread.start()
    

    #result = perplexity("wieviel sind 4 plus 4")
    
    #ergebnis = extrahiere_text(result)
    #print(ergebnis)
    """
    
    
     
    
   

   
    

    
    


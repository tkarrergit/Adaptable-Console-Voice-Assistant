import schriftzug
import funktions
import Tapo
import threading
from PyP100 import PyP100
from PyP100 import PyL530
import ast
from variables_for_all import debug_mode
from variables_for_all import pyttsx_voice_id           
import random
import time
import pyautogui
import show_functions
#Lichtfunktion
from PyP100 import PyP100
from PyP100 import PyL530
global lamp_1, lamp_2

brightness = 50
temp = 2700
farbton = 330
saettigung = 100

dimmzielwert = 0  # Hier kannst du den gewünschten Dimmwert festlegen
dimm_geschwindigkeit = 0.1



startfarbe_d1 = 10
startfarbe_d2 = 10
startfarbe_d3 = 10
startfarbe_d4 = 10
brightness_d1 = 50
brightness_d2 = 50
brightness_d3 = 50
brightness_d4 = 50
start_delay = 1
color_distanz = 15

def get_lamp_by_name(name, lamp_plug_dict):
    return lamp_plug_dict.get(name)

def lamp_dict_func(lamp_1, lamp_2, lamp_3, lamp_4, lamp_5, lamp_6, lamp_7, lamp_8, lamp_9, lamp_10, 
                   lamp_11, lamp_12, lamp_13, lamp_14, lamp_15, lamp_16, lamp_17, lamp_18, lamp_19, 
                   lamp_20, plug_1, plug_2, plug_3, plug_4, plug_5, plug_6, plug_7, plug_8, plug_9, 
                   plug_10, plug_11, plug_12, plug_13, plug_14, plug_15, plug_16, plug_17, plug_18, 
                   plug_19, plug_20):
    lamp_plug_dict = {
                'lamp_1': lamp_1,
                'lamp_2': lamp_2,
                'lamp_3': lamp_3,
                'lamp_4': lamp_4,
                'lamp_5': lamp_5,
                'lamp_6': lamp_6,
                'lamp_7': lamp_7,
                'lamp_8': lamp_8,
                'lamp_9': lamp_9,
                'lamp_10': lamp_10,
                'lamp_11': lamp_11,
                'lamp_12': lamp_12,
                'lamp_13': lamp_13,
                'lamp_14': lamp_14,
                'lamp_15': lamp_15,
                'lamp_16': lamp_16,
                'lamp_17': lamp_17,
                'lamp_18': lamp_18,
                'lamp_19': lamp_19,
                'lamp_20': lamp_20,
                'plug_1': plug_1,
                'plug_2': plug_2,
                'plug_3': plug_3,
                'plug_4': plug_4,
                'plug_5': plug_5,
                'plug_6': plug_6,
                'plug_7': plug_7,
                'plug_8': plug_8,
                'plug_9': plug_9,
                'plug_10': plug_10,
                'plug_11': plug_11,
                'plug_12': plug_12,
                'plug_13': plug_13,
                'plug_14': plug_14,
                'plug_15': plug_15,
                'plug_16': plug_16,
                'plug_17': plug_17,
                'plug_18': plug_18,
                'plug_19': plug_19,
                'plug_20': plug_20
                }
    return lamp_plug_dict




def anschalten_lampe_color(lamp_plug_dict, *lamps, brightness=brightness, farbton=farbton, saettigung=saettigung):
    if debug_mode == True: print("anschalten_lampe_color: ", brightness, farbton, saettigung)
    
    for lamp_name in lamps:
        if debug_mode == True: print(lamp_name)
        
        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOn()
            lamp_plug_object.setColor(farbton, saettigung)
            lamp_plug_object.setBrightness(brightness)
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")
    	
    	
def anschalten_lampe_temp(lamp_plug_dict, *lamps, brightness, temp):
    
    for lamp_name in lamps:
        if debug_mode == True: print(lamp_name)

        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOn()
            lamp_plug_object.setBrightness(brightness)
            lamp_plug_object.setColorTemp(temp)
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")
    	
    	

def ausschalten_lampe(lamp_plug_dict, *lamps):
    
    for lamp_name in lamps:
        if debug_mode == True: print(lamp_name)

        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOff()
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")

        
    	
    	
def anschalten_lampe(lamp_plug_dict, *lamps):
    
    for lamp_name in lamps:
        if debug_mode == True: print(lamp_name)

        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOn()
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")
    	
    	
def anschalten_plugs(lamp_plug_dict, *plugs):
	
    for lamp_name in plugs:
        if debug_mode == True: print(lamp_name)

        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOn()
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")
		
		
def ausschalten_plugs(lamp_plug_dict, *plugs):
	
    for lamp_name in plugs:
        if debug_mode == True: print(lamp_name)

        lamp_plug_object = get_lamp_by_name(lamp_name, lamp_plug_dict)
        if lamp_plug_object is not None:
            lamp_plug_object.turnOff()
        else:
            if debug_mode == True: print(f"Lampe mit dem Namen '{lamp_name}' wurde nicht gefunden.")
		
		
def strahler_slow_fade_out(*lamps, dimmzielwert, dimm_geschwindigkeit, brightness):
    global halb_zaehler, viertel_zaehler
    halb_zaehler = 0
    viertel_zaehler = 0
    bereich = abs(brightness - dimmzielwert)                            # B 100 - D 20= 80
    schritte = int(bereich / 3)                                     # 80 : 4 = 20
    schritte_bereinigt = schritte + 2                               # 20 + 1 = 21
    viertel_schritte = int(schritte_bereinigt / 4)                  # 21 : 4 = 5,25
    if debug_mode == True: print("viertel_schritte = " + str(viertel_schritte))
    hälfte_schritte = int(schritte_bereinigt / 2)                   # 21 : 2 = 10,5
    if debug_mode == True: print("halb_schritte = " + str(hälfte_schritte))
    try:
        if 0 <= dimmzielwert <= 100:
            for lampe in lamps:
                lampe.setBrightness(brightness)       
            
            while schritte_bereinigt >= 1:
                if schritte_bereinigt > hälfte_schritte:
                    if debug_mode == True: print("größer hälfte")
                    brightness = brightness - 3
                    
                    for lampe in lamps:
                        lampe.setBrightness(brightness)            			
                        if debug_mode == True: print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    
                    schritte_bereinigt = schritte_bereinigt - 1
                    if debug_mode == True: print(schritte_bereinigt)
                elif schritte_bereinigt > viertel_schritte:
                    if debug_mode == True: print("größer viertel")
                    brightness = brightness - 2

                    for lampe in lamps:
                        lampe.setBrightness(brightness)                 
                        if debug_mode == True: print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    
                    time.sleep(dimm_geschwindigkeit)

                    if halb_zaehler > abs(viertel_schritte/3):            # 5,25 : 3 =
                        schritte_bereinigt = schritte_bereinigt - 1
                        if debug_mode == True: print(schritte_bereinigt)
                    else:
                        halb_zaehler = halb_zaehler + 1
                        if debug_mode == True: print(halb_zaehler)
                else:
                    brightness = brightness - 1
                    for lampe in lamps:
                        lampe.setBrightness(brightness)
                        if debug_mode == True: print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    time.sleep(abs(dimm_geschwindigkeit))
                    if dimmzielwert == 0 and brightness <= 1:
                        time.sleep(1)
                        for lampe in lamps:
                            ausschalten_lampe(lampe)
                        
                    elif viertel_zaehler > abs((viertel_schritte / 3)*5.4):
                        schritte_bereinigt = schritte_bereinigt - 1
                        if debug_mode == True: print(schritte_bereinigt)
                    else:
                        viertel_zaehler = viertel_zaehler + 1
                        if debug_mode == True: print(viertel_zaehler)

        else:
            print("Ungültige Eingabewerte. Dimmwert muss im Bereich von 0 bis 100 liegen, und Geschwindigkeit muss eine positive Zahl sein.")

    except Exception as e:
            print(f"Error: {e}")

def ultimate_light (tapo_section_name, anschalten_lamp_color, anschalten_lamp_temp, ausschalten_lamp, anschalten_lamp, anschalten_plug, ausschalten_plug, lamp_plug_dict,
                   startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                   color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait):
    print("ULTIMATE_LIGHT: ", brightness, farbton, saettigung)
    config = funktions.configparser.ConfigParser()

    if pyttsx_voice_id == 0:
        config.read(funktions.resource_path('config/German_tapo_config.ini'))  
    if pyttsx_voice_id == 2:
        config.read(funktions.resource_path('config/English_tapo_config.ini'))  
    if pyttsx_voice_id == 4:
        config.read(funktions.resource_path('config/Spanish_tapo_config.ini'))  


    try:
        if anschalten_lamp_color == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("anschalten_lamp_color:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'anschalten_lamp_color_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            anschalten_lampe_color(lamp_plug_dict, *lamps_involved_list, brightness=brightness, farbton=farbton, saettigung=saettigung)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)

        elif anschalten_lamp_temp == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("anschalten_lamp_temp:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'anschalten_lamp_temp_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            anschalten_lampe_temp(lamp_plug_dict, *lamps_involved_list, brightness=brightness, temp=temp)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)

        elif ausschalten_lamp == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("ausschalten_lamp:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'ausschalten_lamp_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            ausschalten_lampe(lamp_plug_dict, *lamps_involved_list)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)

        elif anschalten_lamp == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("anschalten_lamp:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'anschalten_lamp_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            anschalten_lampe(lamp_plug_dict, *lamps_involved_list)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)

        elif anschalten_plug == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("anschalten_plug:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'anschalten_plug_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            anschalten_plugs(lamp_plug_dict, *lamps_involved_list)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)

        elif ausschalten_plug == True:
            if debug_mode == True:print("")
            if debug_mode == True:print("ausschalten_plug:")
            if debug_mode == True:print("")
            # Annahme: Die Lampeninformationen sind als Zeichenkette mit Kommas getrennt gespeichert
            lamps_involved = config.get(tapo_section_name, 'ausschalten_plug_lamps')
            lamps_involved_list = [lamp.strip() for lamp in lamps_involved.split(',')]
            ausschalten_plugs(lamp_plug_dict, *lamps_involved_list)
            if debug_mode == True:print("Beteiligte Lampen:", lamps_involved_list)
            
            
            
            
           

        
    except:
        if debug_mode == True: print("ultimate_light" + f"Error: {e}")        

    
    






def print_functions(functions, debug_mode,): 
    global stop_flag
    while not stop_flag: 
        print(stop_flag)
        # Choose a random function from the list
        random_function = random.choice(functions)
        
        sentence_start = random_function[0]
        sentence_end = random_function[1]
        word = random_function[2]        
        and_word = random_function[3]
        function_description = random_function[4]

        if function_description is not None and len(function_description) >= 3:
            text_1, text_2, text_3 = show_functions.colorize_signal_words(sentence_start, sentence_end, word, and_word, function_description, color=show_functions.ConsoleColors.GREEN)
            show_functions.anzeigen_und_ausblenden(text_1, text_2, text_3, speed=4)
            #if debug_mode == True:funktions.clear_voice_assistent()
        elif stop_flag == True:
            break
        else:
            continue
    


states = {
    'BENUTZER': 0,
    'ASK_TOPIC': 1,
    'ASK_LANG': 2,
    'INIT': 3,
    'ASK_APP': 4,
    'STANDARDUSER': 5,
    'TALKALONG': 6,
}
# Initialize state
current_state = states['STANDARDUSER']
previous_state = states['ASK_LANG']


marker_satz_3 = 'Ask_Topic_espanol:'
random_satz_3 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_3)
marker_satz_4 = 'Ask_Topic_Again_espanol:'
random_satz_4 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_4)
marker_satz_5 = 'Ask_Topic:'
random_satz_5 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_5)
marker_satz_6 = 'Ask_Topic_Again:'
random_satz_6 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_6)
marker_satz_7 = 'Ask_Topic_englisch:'
random_satz_7 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_7)
marker_satz_8 = 'Ask_Topic_Again_englisch:'
random_satz_8 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_8)
marker_satz_9 = 'german_ok:'
random_satz_9 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_9)
marker_satz_10 = 'englisch_ok:'
random_satz_10 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_10)
marker_satz_11 = 'spanisch_ok:'
random_satz_11 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_11)


def chat_dialog(engine):#, App_instance):
    global current_state, previous_state, chatbot, Signal_word_found, vosk_recognizer, pyttsx_voice_id, change_user, stop_flag

    funktions.konsolengroesse(180, 25)
       
    # Erstellen Sie ein ConfigParser-Objekt
    config = funktions.configparser.ConfigParser()

      
       
    pyttsx_voice_id = 2
    change_user_flag = False
    settings_flag = False



    while True:

        try:
            if current_state == states['STANDARDUSER']:                
                
                # Legen Sie den neuen Sektionsnamen fest
                new_section_name = "Standarteinstellungen"
                #Lesen der ini Datei                
                config.read(funktions.resource_path("config/standarduser_config.ini"))
                
                #Lesen der einzelnen Werte aus der ini Datei
                standarduser = config.get(new_section_name, "Benutzer")
                sprache = config.get(new_section_name, "Sprache")
                appnutzung = config.getboolean(new_section_name, "Appnutzung")
                schnellstart = config.getboolean(new_section_name, "schnellstart")
                
                if debug_mode == True: print("standarduser: " +standarduser + " sprache: " + sprache + " appnutzung: " + str(appnutzung) + " schnellstart: " + str(schnellstart))
                

                current_state = states['ASK_LANG']

            if current_state == states['ASK_LANG']:
                if debug_mode == True: print("Ankunft ASK_LANG")
                model = Model(funktions.resource_path(r"zubehoer/vosk-model-small-en-us-0.15"))
                vosk_recognizer = KaldiRecognizer(model, 32000)   
                pyttsx_voice_id = 2
                
                #Wenn es einen Standartsprache in der standartuser_config.ini gibt und keine anfrage auf einen Sprachenwechsel ansteht
                if sprache and change_user_flag == False:
                    user_input = sprache
                    
                    


                if debug_mode == False and not sprache or change_user_flag:
                    funktions.clear_voice_assistent() 
                    #funktions.call_print_function_thread(debug_mode)
                    funktions.print_center_zeile("Choose your prefert language for this Session", 2, "center")               
                    funktions.print_center_zeile("***********************************************", 3, "center") 

                                   
                    #Input ASK_LANG
                    if conn != None:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Do you prefer German, English or Spanish for your Session?")
                        user_input = server_input(conn)
                    else:
                        user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Do you prefer German, English or Spanish for your Session?")                          
                        
                if debug_mode == True or debug_mode == "app":
                    user_input = "deutsch"
                
                #Die Sprache wird in die Standartuser_config.ini geschrieben
                config.set(new_section_name, "Sprache", user_input)                
                with open("config/standarduser_config.ini", "w") as configfile:
                    config.write(configfile)

                if schnellstart == False:
                    if pyttsx_voice_id == 0:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Standart Sprache " + user_input)
                    if pyttsx_voice_id == 2:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Default Language " + user_input)
                    if pyttsx_voice_id == 4:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "idioma predeterminado " + user_input)
                

                if user_input:
                    if user_input.lower() == "deutsch" or user_input.lower() == "german" or user_input.lower() == "aleman":
                        vosk_sprache_deutsch = True
                        vosk_sprache_englisch = False
                        vosk_sprache_spanisch = False
                        pyttsx_voice_id = 0
                        
                        vosk_recognizer = funktions.vosk_sprachepaket_laden(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        pyttsx_voice_id = funktions.pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        
                        
                        if debug_mode == False:funktions.clear_voice_assistent()                                 
                        
                        current_state = states['ASK_APP']
                        continue

                    elif user_input.lower() == "englisch" or user_input.lower() == "english" or user_input.lower() == "ingles":
                        vosk_sprache_deutsch = False
                        vosk_sprache_englisch = True
                        vosk_sprache_spanisch = False
                        pyttsx_voice_id = 2
                        
                        vosk_recognizer = funktions.vosk_sprachepaket_laden(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        pyttsx_voice_id = funktions.pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)                  
                        
                        
                        if debug_mode == False:funktions.clear_voice_assistent()
                        
                        current_state = states['ASK_APP']
                        continue

                    elif user_input.lower() == "spanisch" or user_input.lower() == "spanish" or user_input.lower() == "espanol":
                        vosk_sprache_deutsch = False
                        vosk_sprache_englisch = False
                        vosk_sprache_spanisch = True
                        pyttsx_voice_id = 4
                        
                        vosk_recognizer = funktions.vosk_sprachepaket_laden(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                        pyttsx_voice_id = funktions.pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                 
                        
                        if debug_mode == False:funktions.clear_voice_assistent()
                        current_state = states['ASK_APP']
                        continue

                    else:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Please chose an existing Language we do not offer " + user_input)
                        current_state = states['ASK_LANG']
                        continue

                if debug_mode == False:
                        #funktions.stop_print_function_thread()
                        pass
                
                if not user_input:                    
                    funktions.text_to_speech(engine, pyttsx_voice_id, "Please chose a Language")
                    current_state = states['ASK_LANG']
                    continue      

                    
               

            if current_state == states['ASK_APP']:
                if debug_mode == True: 
                    print("Ankunft ASK_APP")
                    conn = None
                
                user_input = ""
                                    
                  
                if debug_mode == False and settings_flag == True:# or debug_mode == True:
                    while user_input == "":
                         
                        #Input ASK_APP
                        if pyttsx_voice_id == 0:
                            if debug_mode == True:
                                print("Wollen sie die App nutzen?")
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Wollen sie die App nutzen?")
                        if pyttsx_voice_id == 2:
                            if debug_mode == True:
                                print("Do you want to use the App?")
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Do you want to use the App?")
                        if pyttsx_voice_id == 4:
                            if debug_mode == True:
                                print("Quire utilizar el aplication?")
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Quire utilizar el aplication?")
                    
                    if user_input.lower() == "ja" or user_input.lower() == "yes" or user_input.lower() == "si":
                        
                        newappnutzung = True
                        config.set(new_section_name, "Appnutzung", str(newappnutzung))

                        # Schreiben Sie die Konfiguration in eine Datei
                        with open("standarduser_config.ini", "w") as configfile:
                            config.write(configfile)
                        
                        funktions.text_to_speech(engine, pyttsx_voice_id,"Die Appnutzung ist als Standarteinstellung aktiviert")
                        appnutzung = True
                        current_state = states['BENUTZER']       
                    else:
                        newappnutzung = False

                        config.set(new_section_name, "Appnutzung", str(newappnutzung))

                        # Schreiben Sie die Konfiguration in eine Datei
                        with open("standarduser_config.ini", "w") as configfile:
                            config.write(configfile)                     

                        funktions.text_to_speech(engine, pyttsx_voice_id,"Die Appnutzung ist als Standarteinstellung deaktiviert")
                        appnutzung = False
                        conn = None
                        current_state = states['BENUTZER']
                
                if debug_mode == "app" or appnutzung == True:                   
                    
                    if debug_mode == True: print("Please start the App")

                    if pyttsx_voice_id == 0:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Bitte starten sie die App")   
                    if pyttsx_voice_id == 2:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Please start the App")  
                    if pyttsx_voice_id == 4:
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Por favor empieza el aplication")        
                    conn = server.server_program() 
                    current_state = states['BENUTZER']
                
                
                if appnutzung == False:
                    conn = None
                    if schnellstart == False:
                        if pyttsx_voice_id == 0:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Standart Einstellung keine App Nutzung ")
                        if pyttsx_voice_id == 2:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Default Setting no App use")
                        if pyttsx_voice_id == 4:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Configuración por defecto sin uso de la aplicación")
                                    
                current_state = states['BENUTZER']


                
            if current_state == states['BENUTZER']: 
                if debug_mode == True: print("Ankunft BENUTZER")
                                                        
                if debug_mode == False and not standarduser or change_user_flag:
                    funktions.clear_voice_assistent()                                  
                    funktions.print_center_zeile("Please Login to the Adaptable Console Voice Assistant", 2, "center")               
                    funktions.print_center_zeile("*******************************************************", 3, "center") 

                    #Input BENUTZER
                    if pyttsx_voice_id == 0:
                        if conn != None:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Wie ist dein Benutzer Name?")
                            user_input = server_input(conn)
                        else:
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Wie ist dein Benutzer Name?")
                    elif pyttsx_voice_id == 2:
                        if conn != None:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Whats your Username?")
                            user_input = server_input(conn)
                        else:
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Whats your Username?")
                    elif pyttsx_voice_id == 4:
                        if conn != None:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Cuál es tu nombre de usuario?")
                            user_input = server_input(conn)
                        else:
                            user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, "Cuál es tu nombre de usuario?")         
                    benutzername_erfragt = user_input  

                    config.set(new_section_name, "Benutzer", benutzername_erfragt)

                    # Schreiben Sie die Konfiguration in eine Datei
                    with open("config/standarduser_config.ini", "w") as configfile:
                        config.write(configfile)                     

                    funktions.text_to_speech(engine, pyttsx_voice_id,"Der Standartbenutzer ist ab jetzt" + benutzername_erfragt)
                
                #Wenn es einen Standartuser in der standartuser_config.ini gibt und keine anfrage auf einen Benutzerwechsel ansteht
                if standarduser and change_user_flag == False:
                    benutzername_erfragt = standarduser
                    
                    
                if debug_mode == True or debug_mode == "app":
                    print("benutzername_erfragt")          
                    benutzername_erfragt = "thomas"
                    print(benutzername_erfragt)
                            
                # Lese die INI-Datei            
                config.read(funktions.resource_path('config/benutzer_settings_config.ini'))
                
                user_found = False  # Flag to check if a user is found
                
                for i in range(1, 16):
                    
                    # Benutzer_settings_config
                    benutzer_section_name = f'Benutzer_{i}_config'
                    if debug_mode == True: print(benutzer_section_name)
                    benutzername = config.get(benutzer_section_name, 'benutzername')                    
                    tapo_s_ip_1 = config.get(benutzer_section_name, 'tapo_s_ip_1')
                    tapo_s_email_1 = config.get(benutzer_section_name, 'tapo_s_email_1')
                    tapo_s_pass_1 = config.get(benutzer_section_name, 'tapo_s_pass_1')
                    
                    tapo_s_ip_2 = config.get(benutzer_section_name, 'tapo_s_ip_2')
                    tapo_s_email_2 = config.get(benutzer_section_name, 'tapo_s_email_2')
                    tapo_s_pass_2 = config.get(benutzer_section_name, 'tapo_s_pass_2')

                    tapo_s_ip_3 = config.get(benutzer_section_name, 'tapo_s_ip_3')
                    tapo_s_email_3 = config.get(benutzer_section_name, 'tapo_s_email_3')
                    tapo_s_pass_3 = config.get(benutzer_section_name, 'tapo_s_pass_3')

                    tapo_s_ip_4 = config.get(benutzer_section_name, 'tapo_s_ip_4')
                    tapo_s_email_4 = config.get(benutzer_section_name, 'tapo_s_email_4')
                    tapo_s_pass_4 = config.get(benutzer_section_name, 'tapo_s_pass_4')

                    tapo_s_ip_5 = config.get(benutzer_section_name, 'tapo_s_ip_5')
                    tapo_s_email_5 = config.get(benutzer_section_name, 'tapo_s_email_5')
                    tapo_s_pass_5 = config.get(benutzer_section_name, 'tapo_s_pass_5')

                    tapo_s_ip_6 = config.get(benutzer_section_name, 'tapo_s_ip_6')
                    tapo_s_email_6 = config.get(benutzer_section_name, 'tapo_s_email_6')
                    tapo_s_pass_6 = config.get(benutzer_section_name, 'tapo_s_pass_6')

                    tapo_s_ip_7 = config.get(benutzer_section_name, 'tapo_s_ip_7')
                    tapo_s_email_7 = config.get(benutzer_section_name, 'tapo_s_email_7')
                    tapo_s_pass_7 = config.get(benutzer_section_name, 'tapo_s_pass_7')

                    tapo_s_ip_8 = config.get(benutzer_section_name, 'tapo_s_ip_8')
                    tapo_s_email_8 = config.get(benutzer_section_name, 'tapo_s_email_8')
                    tapo_s_pass_8 = config.get(benutzer_section_name, 'tapo_s_pass_8')

                    tapo_s_ip_9 = config.get(benutzer_section_name, 'tapo_s_ip_9')
                    tapo_s_email_9 = config.get(benutzer_section_name, 'tapo_s_email_9')
                    tapo_s_pass_9 = config.get(benutzer_section_name, 'tapo_s_pass_9')

                    tapo_s_ip_10 = config.get(benutzer_section_name, 'tapo_s_ip_10')
                    tapo_s_email_10 = config.get(benutzer_section_name, 'tapo_s_email_10')
                    tapo_s_pass_10 = config.get(benutzer_section_name, 'tapo_s_pass_10')

                    tapo_s_ip_11 = config.get(benutzer_section_name, 'tapo_s_ip_11')
                    tapo_s_email_11 = config.get(benutzer_section_name, 'tapo_s_email_11')
                    tapo_s_pass_11 = config.get(benutzer_section_name, 'tapo_s_pass_11')

                    tapo_s_ip_12 = config.get(benutzer_section_name, 'tapo_s_ip_12')
                    tapo_s_email_12 = config.get(benutzer_section_name, 'tapo_s_email_12')
                    tapo_s_pass_12 = config.get(benutzer_section_name, 'tapo_s_pass_12')

                    tapo_s_ip_13 = config.get(benutzer_section_name, 'tapo_s_ip_13')
                    tapo_s_email_13 = config.get(benutzer_section_name, 'tapo_s_email_13')
                    tapo_s_pass_13 = config.get(benutzer_section_name, 'tapo_s_pass_13')

                    tapo_s_ip_14 = config.get(benutzer_section_name, 'tapo_s_ip_14')
                    tapo_s_email_14 = config.get(benutzer_section_name, 'tapo_s_email_14')
                    tapo_s_pass_14 = config.get(benutzer_section_name, 'tapo_s_pass_14')

                    tapo_s_ip_15 = config.get(benutzer_section_name, 'tapo_s_ip_15')
                    tapo_s_email_15 = config.get(benutzer_section_name, 'tapo_s_email_15')
                    tapo_s_pass_15 = config.get(benutzer_section_name, 'tapo_s_pass_15')

                    tapo_s_ip_16 = config.get(benutzer_section_name, 'tapo_s_ip_16')
                    tapo_s_email_16 = config.get(benutzer_section_name, 'tapo_s_email_16')
                    tapo_s_pass_16 = config.get(benutzer_section_name, 'tapo_s_pass_16')

                    tapo_s_ip_17 = config.get(benutzer_section_name, 'tapo_s_ip_17')
                    tapo_s_email_17 = config.get(benutzer_section_name, 'tapo_s_email_17')
                    tapo_s_pass_17 = config.get(benutzer_section_name, 'tapo_s_pass_17')

                    tapo_s_ip_18 = config.get(benutzer_section_name, 'tapo_s_ip_18')
                    tapo_s_email_18 = config.get(benutzer_section_name, 'tapo_s_email_18')
                    tapo_s_pass_18 = config.get(benutzer_section_name, 'tapo_s_pass_18')

                    tapo_s_ip_19 = config.get(benutzer_section_name, 'tapo_s_ip_19')
                    tapo_s_email_19 = config.get(benutzer_section_name, 'tapo_s_email_19')
                    tapo_s_pass_19 = config.get(benutzer_section_name, 'tapo_s_pass_19')

                    tapo_s_ip_20 = config.get(benutzer_section_name, 'tapo_s_ip_20')
                    tapo_s_email_20 = config.get(benutzer_section_name, 'tapo_s_email_20')
                    tapo_s_pass_20 = config.get(benutzer_section_name, 'tapo_s_pass_20')
                    

                    tapo_p_ip_1 = config.get(benutzer_section_name, 'tapo_p_ip_1')
                    tapo_p_email_1 = config.get(benutzer_section_name, 'tapo_p_email_1')
                    tapo_p_pass_1 = config.get(benutzer_section_name, 'tapo_p_pass_1')

                    tapo_p_ip_2 = config.get(benutzer_section_name, 'tapo_p_ip_2')
                    tapo_p_email_2 = config.get(benutzer_section_name, 'tapo_p_email_2')
                    tapo_p_pass_2 = config.get(benutzer_section_name, 'tapo_p_pass_2')

                    tapo_p_ip_3 = config.get(benutzer_section_name, 'tapo_p_ip_3')
                    tapo_p_email_3 = config.get(benutzer_section_name, 'tapo_p_email_3')
                    tapo_p_pass_3 = config.get(benutzer_section_name, 'tapo_p_pass_3')

                    tapo_p_ip_4 = config.get(benutzer_section_name, 'tapo_p_ip_4')
                    tapo_p_email_4 = config.get(benutzer_section_name, 'tapo_p_email_4')
                    tapo_p_pass_4 = config.get(benutzer_section_name, 'tapo_p_pass_4')

                    tapo_p_ip_5 = config.get(benutzer_section_name, 'tapo_p_ip_5')
                    tapo_p_email_5 = config.get(benutzer_section_name, 'tapo_p_email_5')
                    tapo_p_pass_5 = config.get(benutzer_section_name, 'tapo_p_pass_5')

                    tapo_p_ip_6 = config.get(benutzer_section_name, 'tapo_p_ip_6')
                    tapo_p_email_6 = config.get(benutzer_section_name, 'tapo_p_email_6')
                    tapo_p_pass_6 = config.get(benutzer_section_name, 'tapo_p_pass_6')

                    tapo_p_ip_7 = config.get(benutzer_section_name, 'tapo_p_ip_7')
                    tapo_p_email_7 = config.get(benutzer_section_name, 'tapo_p_email_7')
                    tapo_p_pass_7 = config.get(benutzer_section_name, 'tapo_p_pass_7')

                    tapo_p_ip_8 = config.get(benutzer_section_name, 'tapo_p_ip_8')
                    tapo_p_email_8 = config.get(benutzer_section_name, 'tapo_p_email_8')
                    tapo_p_pass_8 = config.get(benutzer_section_name, 'tapo_p_pass_8')

                    tapo_p_ip_9 = config.get(benutzer_section_name, 'tapo_p_ip_9')
                    tapo_p_email_9 = config.get(benutzer_section_name, 'tapo_p_email_9')
                    tapo_p_pass_9 = config.get(benutzer_section_name, 'tapo_p_pass_9')

                    tapo_p_ip_10 = config.get(benutzer_section_name, 'tapo_p_ip_10')
                    tapo_p_email_10 = config.get(benutzer_section_name, 'tapo_p_email_10')
                    tapo_p_pass_10 = config.get(benutzer_section_name, 'tapo_p_pass_10')

                    tapo_p_ip_11 = config.get(benutzer_section_name, 'tapo_p_ip_11')
                    tapo_p_email_11 = config.get(benutzer_section_name, 'tapo_p_email_11')
                    tapo_p_pass_11 = config.get(benutzer_section_name, 'tapo_p_pass_11')

                    tapo_p_ip_12 = config.get(benutzer_section_name, 'tapo_p_ip_12')
                    tapo_p_email_12 = config.get(benutzer_section_name, 'tapo_p_email_12')
                    tapo_p_pass_12 = config.get(benutzer_section_name, 'tapo_p_pass_12')

                    tapo_p_ip_13 = config.get(benutzer_section_name, 'tapo_p_ip_13')
                    tapo_p_email_13 = config.get(benutzer_section_name, 'tapo_p_email_13')
                    tapo_p_pass_13 = config.get(benutzer_section_name, 'tapo_p_pass_13')

                    tapo_p_ip_14 = config.get(benutzer_section_name, 'tapo_p_ip_14')
                    tapo_p_email_14 = config.get(benutzer_section_name, 'tapo_p_email_14')
                    tapo_p_pass_14 = config.get(benutzer_section_name, 'tapo_p_pass_14')

                    tapo_p_ip_15 = config.get(benutzer_section_name, 'tapo_p_ip_15')
                    tapo_p_email_15 = config.get(benutzer_section_name, 'tapo_p_email_15')
                    tapo_p_pass_15 = config.get(benutzer_section_name, 'tapo_p_pass_15')

                    tapo_p_ip_16 = config.get(benutzer_section_name, 'tapo_p_ip_16')
                    tapo_p_email_16 = config.get(benutzer_section_name, 'tapo_p_email_16')
                    tapo_p_pass_16 = config.get(benutzer_section_name, 'tapo_p_pass_16')

                    tapo_p_ip_17 = config.get(benutzer_section_name, 'tapo_p_ip_17')
                    tapo_p_email_17 = config.get(benutzer_section_name, 'tapo_p_email_17')
                    tapo_p_pass_17 = config.get(benutzer_section_name, 'tapo_p_pass_17')

                    tapo_p_ip_18 = config.get(benutzer_section_name, 'tapo_p_ip_18')
                    tapo_p_email_18 = config.get(benutzer_section_name, 'tapo_p_email_18')
                    tapo_p_pass_18 = config.get(benutzer_section_name, 'tapo_p_pass_18')

                    tapo_p_ip_19 = config.get(benutzer_section_name, 'tapo_p_ip_19')
                    tapo_p_email_19 = config.get(benutzer_section_name, 'tapo_p_email_19')
                    tapo_p_pass_19 = config.get(benutzer_section_name, 'tapo_p_pass_19')

                    tapo_p_ip_20 = config.get(benutzer_section_name, 'tapo_p_ip_20')
                    tapo_p_email_20 = config.get(benutzer_section_name, 'tapo_p_email_20')
                    tapo_p_pass_20 = config.get(benutzer_section_name, 'tapo_p_pass_20')                         
                    
                    
                    if funktions.contains_benutzername(benutzername_erfragt, benutzername):                        
                        if debug_mode == False and not standarduser: 
                            funktions.text_to_speech(engine, pyttsx_voice_id, benutzername)
                        if schnellstart == False:
                            if standarduser:
                                if pyttsx_voice_id == 0:
                                    funktions.text_to_speech(engine, pyttsx_voice_id, "Standartbenutzer: " +benutzername)
                                if pyttsx_voice_id == 2:
                                    funktions.text_to_speech(engine, pyttsx_voice_id, "Default User: " +benutzername)
                                if pyttsx_voice_id == 4:
                                    funktions.text_to_speech(engine, pyttsx_voice_id, "Usuario predeterminado: " +benutzername)
                        
                        if schnellstart == False:
                            if pyttsx_voice_id == 0:
                                funktions.print_center_zeile("Standarteinstellungen ändern", 2, "center")
                                funktions.print_center_zeile("******************************", 3, "center")
                                funktions.text_to_speech(engine, pyttsx_voice_id, "Nach dem Start des Assistenten kannst du den Benutzer oder die Sprache wechseln indem du Benutzer oder Sprache sagst. Zum ändern der App einstellungen sag Einstellungen")
                    
                                            
                            if pyttsx_voice_id == 2:
                                funktions.text_to_speech(engine, pyttsx_voice_id, "After starting the assistant, you can change the user or language by saying User or Language. To change the app settings, say Settings")
                                funktions.print_center_zeile("Change default settings", 2, "center")
                                funktions.print_center_zeile("*************************", 3, "center")
                                
                            if pyttsx_voice_id == 4:
                                funktions.text_to_speech(engine, pyttsx_voice_id, "Después de iniciar el asistente, puedes cambiar el usuario o el idioma diciendo Usuario o Idioma. Para cambiar los ajustes de la aplicación, diga configuración")
                                funktions.print_center_zeile("Cambiar la configuración predeterminada", 2, "center")
                                funktions.print_center_zeile("*****************************************", 3, "center")
                                                    
                                                
                        if change_user_flag == True:
                            current_state = states['INIT']
                        else:
                            current_state = states['INIT']
                        user_found = True  # Set the flag to True if a user is found                         
                        break

                    

                if not user_found:
                    funktions.text_to_speech(engine, pyttsx_voice_id, benutzername_erfragt + " is no registrated user.")
                    current_state = states['BENUTZER']
                    if debug_mode == True: print("keine übereinstimmung")                                         
            
            if debug_mode == True: print("Ankunft lamp_1")
            lamp_1 = PyL530.L530(tapo_s_ip_1, tapo_s_email_1, tapo_s_pass_1)
            lamp_2 = PyL530.L530(tapo_s_ip_2, tapo_s_email_2, tapo_s_pass_2)
            lamp_3 = PyL530.L530(tapo_s_ip_3, tapo_s_email_3, tapo_s_pass_3)
            lamp_4 = PyL530.L530(tapo_s_ip_4, tapo_s_email_4, tapo_s_pass_4)
            lamp_5 = PyL530.L530(tapo_s_ip_5, tapo_s_email_5, tapo_s_pass_5)
            lamp_6 = PyL530.L530(tapo_s_ip_6, tapo_s_email_6, tapo_s_pass_6)
            lamp_7 = PyL530.L530(tapo_s_ip_7, tapo_s_email_7, tapo_s_pass_7)
            lamp_8 = PyL530.L530(tapo_s_ip_8, tapo_s_email_8, tapo_s_pass_8)
            lamp_9 = PyL530.L530(tapo_s_ip_9, tapo_s_email_9, tapo_s_pass_9)
            lamp_10 = PyL530.L530(tapo_s_ip_10, tapo_s_email_10, tapo_s_pass_10)
            lamp_11 = PyL530.L530(tapo_s_ip_11, tapo_s_email_11, tapo_s_pass_11)
            lamp_12 = PyL530.L530(tapo_s_ip_12, tapo_s_email_12, tapo_s_pass_12)
            lamp_13 = PyL530.L530(tapo_s_ip_13, tapo_s_email_13, tapo_s_pass_13)
            lamp_14 = PyL530.L530(tapo_s_ip_14, tapo_s_email_14, tapo_s_pass_14)
            lamp_15 = PyL530.L530(tapo_s_ip_15, tapo_s_email_15, tapo_s_pass_15)
            lamp_16 = PyL530.L530(tapo_s_ip_16, tapo_s_email_16, tapo_s_pass_16)
            lamp_17 = PyL530.L530(tapo_s_ip_17, tapo_s_email_17, tapo_s_pass_17)
            lamp_18 = PyL530.L530(tapo_s_ip_18, tapo_s_email_18, tapo_s_pass_18)
            lamp_19 = PyL530.L530(tapo_s_ip_19, tapo_s_email_19, tapo_s_pass_19)
            lamp_20 = PyL530.L530(tapo_s_ip_20, tapo_s_email_20, tapo_s_pass_20)
                 
            plug_1 = PyP100.P100(tapo_p_ip_1, tapo_p_email_1, tapo_p_pass_1)
            plug_2 = PyP100.P100(tapo_p_ip_2, tapo_p_email_2, tapo_p_pass_2)
            plug_3 = PyP100.P100(tapo_p_ip_3, tapo_p_email_3, tapo_p_pass_3)
            plug_4 = PyP100.P100(tapo_p_ip_4, tapo_p_email_4, tapo_p_pass_4)
            plug_5 = PyP100.P100(tapo_p_ip_5, tapo_p_email_5, tapo_p_pass_5)
            plug_6 = PyP100.P100(tapo_p_ip_6, tapo_p_email_6, tapo_p_pass_6)
            plug_7 = PyP100.P100(tapo_p_ip_7, tapo_p_email_7, tapo_p_pass_7)
            plug_8 = PyP100.P100(tapo_p_ip_8, tapo_p_email_8, tapo_p_pass_8)
            plug_9 = PyP100.P100(tapo_p_ip_9, tapo_p_email_9, tapo_p_pass_9)
            plug_10 = PyP100.P100(tapo_p_ip_10, tapo_p_email_10, tapo_p_pass_10)
            plug_11 = PyP100.P100(tapo_p_ip_11, tapo_p_email_11, tapo_p_pass_11)
            plug_12 = PyP100.P100(tapo_p_ip_12, tapo_p_email_12, tapo_p_pass_12)
            plug_13 = PyP100.P100(tapo_p_ip_13, tapo_p_email_13, tapo_p_pass_13)
            plug_14 = PyP100.P100(tapo_p_ip_14, tapo_p_email_14, tapo_p_pass_14)
            plug_15 = PyP100.P100(tapo_p_ip_15, tapo_p_email_15, tapo_p_pass_15)
            plug_16 = PyP100.P100(tapo_p_ip_16, tapo_p_email_16, tapo_p_pass_16)
            plug_17 = PyP100.P100(tapo_p_ip_17, tapo_p_email_17, tapo_p_pass_17)
            plug_18 = PyP100.P100(tapo_p_ip_18, tapo_p_email_18, tapo_p_pass_18)
            plug_19 = PyP100.P100(tapo_p_ip_19, tapo_p_email_19, tapo_p_pass_19)
            plug_20 = PyP100.P100(tapo_p_ip_20, tapo_p_email_20, tapo_p_pass_20)

            lamp_dict_func(lamp_1, lamp_2, lamp_3, lamp_4, lamp_5, lamp_6, lamp_7, lamp_8, lamp_9, lamp_10, 
                   lamp_11, lamp_12, lamp_13, lamp_14, lamp_15, lamp_16, lamp_17, lamp_18, lamp_19, 
                   lamp_20, plug_1, plug_2, plug_3, plug_4, plug_5, plug_6, plug_7, plug_8, plug_9, 
                   plug_10, plug_11, plug_12, plug_13, plug_14, plug_15, plug_16, plug_17, plug_18, 
                   plug_19, plug_20)
            
            
                        

            if current_state == states['INIT']:
                #model = Model(funktions.resource_path(r"zubehoer/vosk-model-small-en-us-0.15"))
                #vosk_recognizer = KaldiRecognizer(model, 32000)  
                
                #pyttsx_voice_id = 2  
                
                if debug_mode == False:funktions.clear_voice_assistent() 
                

                #functions = funktions.function_collection(0) 
                #stop_flag = False   
                #print_functions_thread = threading.Thread(target=print_functions, args=(functions, debug_mode,)
                #print_functions_thread.start()
                
                if debug_mode == False:
                    #funktions.call_print_function_thread(debug_mode)
                    if pyttsx_voice_id == 0:
                        #schriftzug.call_schriftzug_thread()
                        funktions.print_center_zeile("Willkommen zum Adaptable Console Voice Assistant", 2, "center")
                        funktions.print_center_zeile("***************************************************", 3, "center")  
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Willkommen zum Anpassbaren Konsolen Sprachassistenten. Lass uns starten!")
                        time.sleep(0.2)
                        #pyautogui.press("q")

                    if pyttsx_voice_id == 2:
                        funktions.print_center_zeile("me to the Adaptable Console Voice Assistant", 2, "center")
                        funktions.print_center_zeile("***************************************************", 3, "center")  
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Welcome, to the Adaptable Console Voice Assistant. Son we will start!")#Your creative artist for the ultimate digital lifestyle! With a single voice command, ignite a fireworks display of features from personalized app interactions, to individual stories and soothing sounds. Experience the freedom of customization and the security, of offline speech recognition. Let's get started!")           
                            
                    if pyttsx_voice_id == 4:
                        funktions.print_center_zeile("Bienvenidos a Adaptable Console Voice Assistant", 2, "center")
                        funktions.print_center_zeile("***************************************************", 3, "center")  
                        funktions.text_to_speech(engine, pyttsx_voice_id, "Bienvenidos a Adaptable Console Voice Assistant. Un momento, y Vamonos!")
                                         
                              
                    #schriftzug.stop_schriftzug_thread()
                    #funktions.stop_print_function_thread() 

                if debug_mode == True:
                    current_state = states['ASK_TOPIC']
                else:
                    current_state = states['ASK_TOPIC']        
            
                
                


            

            if current_state == states['ASK_TOPIC']:
                if debug_mode == True: print("Ankunft ASK_TOPIC")
                #vosk_recognizer = funktions.vosk_sprachepaket_laden(vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                #pyttsx_voice_id = funktions.pyttsx3_voice_sprache(engine, vosk_sprache_deutsch, vosk_sprache_englisch, vosk_sprache_spanisch)
                if debug_mode == False:
                    print_flag = False 
                    funktions.clear_voice_assistent()
                    #if funktions.print_functions_thread.is_alive():
                        #print_flag = True
                    #elif print_flag == False:
                    #funktions.call_print_function_thread(debug_mode)
                    funktions.print_center_zeile("Choose one of your own created creative functions and have fun!", 2, "center")               
                    funktions.print_center_zeile("****************************************************************", 3, "center")
                    
                if pyttsx_voice_id == 0:
                    if debug_mode == True:print("Deutsche Dateien geladen")
                    additional_config_paths = [
                        funktions.resource_path('config/German_app_config.ini'),
                        funktions.resource_path('config/German_tapo_config.ini'),
                        funktions.resource_path('config/German_chat_config.ini'),
                        funktions.resource_path('config/German_combination_config.ini'),
                        funktions.resource_path('config/German_system_functions.ini')           
                    ]
                    config.read(additional_config_paths)
                    
                elif pyttsx_voice_id == 2:
                    if debug_mode == True:print("Englische Dateien geladen")
                    additional_config_paths = [            
                        funktions.resource_path('config/English_app_config.ini'),
                        funktions.resource_path('config/English_tapo_config.ini'),
                        funktions.resource_path('config/English_chat_config.ini'),
                        funktions.resource_path('config/English_combination_config.ini')
                        ]    
                    config.read(additional_config_paths)
                    
                elif pyttsx_voice_id == 4:
                    if debug_mode == True:print("Spanische Dateien geladen")
                    additional_config_paths = [            
                        funktions.resource_path('config/Spanish_app_config.ini'),
                        funktions.resource_path('config/Spanish_tapo_config.ini'),
                        funktions.resource_path('config/Spanish_chat_config.ini'),
                        funktions.resource_path('config/Spanish_combination_config.ini'),
                        # Füge hier die Pfade für die restlichen Config-Dateien hinzu
                    ]
                    config.read(additional_config_paths)

                if debug_mode == True:print(pyttsx_voice_id)

                marker_satz_3 = 'Ask_Topic_espanol:'
                random_satz_3 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_3)
                marker_satz_4 = 'Ask_Topic_Again_espanol:'
                random_satz_4 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_4)
                marker_satz_5 = 'Ask_Topic:'
                random_satz_5 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_5)
                marker_satz_6 = 'Ask_Topic_Again:'
                random_satz_6 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_6)
                marker_satz_7 = 'Ask_Topic_englisch:'
                random_satz_7 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_7)
                marker_satz_8 = 'Ask_Topic_Again_englisch:'
                random_satz_8 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_8)

                random_satz_1, random_satz_2 = funktions.unterschied_sprache_random_satz(random_satz_5, random_satz_6, random_satz_3, random_satz_4, random_satz_7, random_satz_8, pyttsx_voice_id)
                
                if debug_mode == True: print("random Satz: " + random_satz_1 + random_satz_2)
                current_ask_topic_sentence = random_satz_2 
                
                #Input ASK_TOPIC
                if debug_mode == True:
                    conn = None
                if conn != None:                    
                    user_input = server_input(conn)
                    print("Anfrage von App" + user_input)
                else:
                    #########################################################################################################################
                    #user_input = funktions.text_to_speech_and_listen(engine, vosk_recognizer, pyttsx_voice_id, {current_ask_topic_sentence})
                    ##########################################################################################################################
                    user_input = input("Was kann ich für dich tun?")
                #Standarteinstellungen ändern
                if "einstellungen" in user_input.lower() or "settings" in user_input.lower() or "configuración" in user_input.lower():
                    settings_flag = True
                    current_state = states['ASK_APP']
                    continue

                if debug_mode == True: print("Sections:", config.sections())
                Signal_word_found = False  

                

                for i in range(1, 16):
                    
                    if pyttsx_voice_id == 0:
                        ChatSettings = "ChatSettings"
                        AppSettings = "AppSettings"
                        TapoSettings = "TapoSettings"
                        CombinationSettings = "CombinationSettings"
                    if pyttsx_voice_id == 2:
                        ChatSettings = "English_ChatSettings"
                        AppSettings = "English_AppSettings"
                        TapoSettings = "English_TapoSettings"
                        CombinationSettings = "English_CombinationSettings"
                    if pyttsx_voice_id == 4:
                        ChatSettings = "Spanish_ChatSettings"
                        AppSettings = "Spanish_AppSettings"
                        TapoSettings = "Spanish_TapoSettings"
                        CombinationSettings = "Spanish_CombinationSettings"

                    if debug_mode == True:print("German Settings")
                    # German
                    # ChatSettings Conf
                    section_name = f'{ChatSettings} Funktion {i}'                        
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
                    app_section_name = f'{AppSettings} Funktion {i}'
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
                    tapo_section_name = f'{TapoSettings}_Funktion_{i}'
                    tapo_signal_words = config.get(tapo_section_name, 'tapo_signal_word')
                    tapo_and_signal_words = config.get(tapo_section_name, 'tapo_and_signal_word')
                    # Effekte und Funktionen für Strahler
                    anschalten_lamp_color = config.getboolean(tapo_section_name, 'anschalten_lamp_color')
                    anschalten_lamp_temp = config.getboolean(tapo_section_name, 'anschalten_lamp_temp')                    
                    anschalten_lamp = config.getboolean(tapo_section_name, 'anschalten_lamp')
                    ausschalten_lamp = config.getboolean(tapo_section_name, 'ausschalten_lamp')                      
                    #Funktionen für Plug´s
                    anschalten_plug = config.getboolean(tapo_section_name, 'anschalten_plug')                      
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
                    combination_section_name = f'{CombinationSettings}_Funktion_{i}'
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

                    #System_Function
                    section_name = f'system_functions_{i}'
                    change_language = config.get(section_name, 'change_language')
                    change_user = config.get(section_name, 'change_user')
                    
                    if debug_mode == False:
                      #  funktions_function_thread()
                      pass
                 
                    #Change User or Language
                    if debug_mode == True: print("chat_dialog Unterfunktion chanhge User language: ")  
                    contains_change_user_or_language = funktions.contains_change_user_or_language(user_input, change_language, change_user, section_name)                    
                    if debug_mode == True: print("Chat_Dialog: contains_change_user_or_language: " + str(contains_change_user_or_language))
                    if contains_change_user_or_language != False: 
                        if pyttsx_voice_id == 0:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Gerne")
                            
                        elif pyttsx_voice_id == 2:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "your welcome")
                            
                        elif pyttsx_voice_id == 4:
                            funktions.text_to_speech(engine, pyttsx_voice_id, "Sie claro")
                            
                            
                        current_state = funktions.change_user_or_language(contains_change_user_or_language) 
                        change_user_flag = True

                    


                    #Zusammensetzen des User_input_i für die GPT anfragen mit und ohne user_input und zusätzlich bestehend aus den 7 bestandteilen eines guten Promts.
                    if user_input_enabled:
                        user_input_i = user_input + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    else:
                        user_input_i = user_input_task + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    lamp_plug_dict = lamp_dict_func(lamp_1, lamp_2, lamp_3, lamp_4, lamp_5, lamp_6, lamp_7, lamp_8, lamp_9, lamp_10, 
                                                    lamp_11, lamp_12, lamp_13, lamp_14, lamp_15, lamp_16, lamp_17, lamp_18, lamp_19, 
                                                    lamp_20, plug_1, plug_2, plug_3, plug_4, plug_5, plug_6, plug_7, plug_8, plug_9, 
                                                    plug_10, plug_11, plug_12, plug_13, plug_14, plug_15, plug_16, plug_17, plug_18, 
                                                    plug_19, plug_20)
                    
                    if funktions.combination_contains_signal_word(user_input, combination_signal_words, combination_and_signal_words): 
                        marker_satz_9 = 'german_ok:'
                        random_satz_9 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_9)
                        marker_satz_10 = 'englisch_ok:'
                        random_satz_10 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_10)
                        marker_satz_11 = 'spanisch_ok:'
                        random_satz_11 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_11)   

                        ok_satz = funktions.unterschied_sprache_ein_random_satz(random_satz_9, random_satz_10, random_satz_11, pyttsx_voice_id)
                        funktions.text_to_speech(engine, pyttsx_voice_id, ok_satz)
                      
                        if debug_mode == False:funktions.clear_voice_assistent()
                        Signal_word_found = True
                        funktions.ultimate_combination(lamp_plug_dict, user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
                                            user_combination_input_7, user_combination_input_8, user_combination_input_9, user_combination_input_10, signal_words, and_signal_words, section_name, dialog_chat_enabled, 
                                            app_signal_words, app_and_signal_words, app_section_name, app, mouse_click_on_coordinates_1, mouse_click_on_coordinates_2, mouse_click_on_coordinates_3, 
                                               mouse_click_on_coordinates_4, mouse_click_on_coordinates_5, mouse_click_on_coordinates_6, 
                                               double_mouse_click_on_coordinates_1, double_mouse_click_on_coordinates_2,
                                               double_mouse_click_on_coordinates_3, double_mouse_click_on_coordinates_4, 
                                               double_mouse_click_on_coordinates_5, double_mouse_click_on_coordinates_6, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup, wait_app,
                                            wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                            wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3, text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                            keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list, user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                            user_input_enabled_4, user_input_enabled_5, user_input_enabled_6, tapo_signal_words, tapo_and_signal_words, tapo_section_name, 
                                            anschalten_lamp_color, anschalten_lamp_temp, ausschalten_lamp, anschalten_lamp, anschalten_plug, ausschalten_plug,                          
                                            startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                                            color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait, engine, vosk_recognizer)
                        
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']
                        break
                        
                    elif funktions.contains_signal_word(user_input, signal_words, and_signal_words, section_name):
                        marker_satz_9 = 'german_ok:'
                        random_satz_9 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_9)
                        marker_satz_10 = 'englisch_ok:'
                        random_satz_10 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_10)
                        marker_satz_11 = 'spanisch_ok:'
                        random_satz_11 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_11)
                        ok_satz = funktions.unterschied_sprache_ein_random_satz(random_satz_9, random_satz_10, random_satz_11, pyttsx_voice_id)

                        #Output
                        if conn != None:
                            if debug_mode == True:
                                print("Output Server")
                            server.server_output(conn, ok_satz)
                        else:
                            funktions.text_to_speech(engine, pyttsx_voice_id, ok_satz)
                                               
                        #if debug_mode == False:funktions.clear_voice_assistent()
                        Signal_word_found = True
                        if dialog_chat_enabled:
                            if conn != None:
                                if debug_mode == True:
                                    print("Output Server")
                                server.server_output(conn, "dialogmodus")
                            if debug_mode ==False:
                                funktions.print_center_zeile("Dialogmodus wird gestartet. Einen kleinen Augenblick bitte.", 1, "left")

                            if active_chat_engine=="huggingface":
                                try:                                    
                                    funktions.huggingface_newchat(chatbot)
                                except:
                                    if conn != None:
                                        server.server_output(conn, "Verbindungs- oder Serverprobleme bitte versuch es später nochmal ")
                                    else:
                                        funktions.text_to_speech(engine, pyttsx_voice_id, "Verbindungs- oder Serverprobleme bitte versuch es später nochmal ")

                            while True:
                                if debug_mode == True: 
                                    print(user_input_i)
                                if debug_mode ==False: 
                                    funktions.print_center_zeile("Dialogmodus", 1, "left")
                                if debug_mode == True: 
                                    print("Dialogmodus")
                               
                                funktions.process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id, conn, section_name)
                                
                                if debug_mode == True: print("process_user_input fertiggestellt")
                                if debug_mode == True: print("Erster user_input_i: " + user_input_i)

                               
                                #Input Dialogmodus
                                if conn != None:
                                    user_input_i = server_input(conn)
                                else:
                                    user_input_i = funktions.get_user_input(vosk_recognizer)

                                if debug_mode == True: print("Folgender user_input_i: " + user_input_i)
                                if "qq" in user_input_i.lower() or "stopp" in user_input_i.lower() or "es reicht" in user_input_i.lower() or "stop" in user_input_i.lower() or "parar" in user_input_i.lower():
                                    #Bei dieser Funktion wird nichts an die Client App geschickt, da die Funktion direkt in der Clien App umgesetzt ist
                                    if pyttsx_voice_id == 0:
                                        funktions.text_to_speech(engine, pyttsx_voice_id, "Danke, war ein gutes Gespräch")
                                    elif pyttsx_voice_id == 2:                                        
                                        funktions.text_to_speech(engine, pyttsx_voice_id, "Ok, thank you for the nice conversation")
                                    elif pyttsx_voice_id == 4:                                        
                                        funktions.text_to_speech(engine, pyttsx_voice_id, "Sie claro, gracias por la buen conversación")
                                        
                                    if debug_mode == False:funktions.clear_voice_assistent()                                    
                                    current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                                    
                                    previous_state = states['ASK_TOPIC']
                                    break
                        else:                                                                                
                            funktions.process_user_input(engine, active_chat_engine, user_input_i, chatbot, pyttsx_voice_id, conn, section_name)
                            current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                            previous_state = states['ASK_TOPIC']
                            break

                    elif funktions.app_contains_signal_word(user_input, app_signal_words, app_and_signal_words, app_section_name):
                        marker_satz_9 = 'german_ok:'
                        random_satz_9 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_9)
                        marker_satz_10 = 'englisch_ok:'
                        random_satz_10 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_10)
                        marker_satz_11 = 'spanisch_ok:'
                        random_satz_11 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_11)
                        ok_satz = funktions.unterschied_sprache_ein_random_satz(random_satz_9, random_satz_10, random_satz_11, pyttsx_voice_id)

                        if conn != None:
                            if debug_mode == True:
                                print("Output Server")
                            server.server_output(conn, ok_satz)
                        else:
                            funktions.text_to_speech(engine, pyttsx_voice_id, ok_satz)

                        Signal_word_found = True
                        if debug_mode == True: print("App Funktion")
                        user_input_app = funktions.input_app(user_input, app_signal_words, app_and_signal_words)
                        if debug_mode == True:print(user_input_app)
                        
                        if debug_mode == False:funktions.clear_voice_assistent()
                        funktions.app_ultimate(app, [mouse_click_on_coordinates_1, mouse_click_on_coordinates_2, mouse_click_on_coordinates_3, 
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
                        
                        previous_state = states['ASK_TOPIC']
                        break
                        
                    elif funktions.tapo_contains_signal_word(user_input, tapo_signal_words, tapo_and_signal_words, tapo_section_name):
                        marker_satz_9 = 'german_ok:'
                        random_satz_9 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_9)
                        marker_satz_10 = 'englisch_ok:'
                        random_satz_10 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_10)
                        marker_satz_11 = 'spanisch_ok:'
                        random_satz_11 = funktions.get_random_sentence_from_file(funktions.file_path_satz, marker_satz_11)
                        ok_satz = funktions.unterschied_sprache_ein_random_satz(random_satz_9, random_satz_10, random_satz_11, pyttsx_voice_id)

                        if conn != None:
                            if debug_mode == True:
                                print("Output Server")
                            server.server_output(conn, ok_satz)
                        else:
                            funktions.text_to_speech(engine, pyttsx_voice_id, ok_satz)

                        Signal_word_found = True
                        
                        threading.Thread(target=ultimate_light, daemon=True, args=(tapo_section_name, anschalten_lamp_color, anschalten_lamp_temp, ausschalten_lamp, anschalten_lamp, anschalten_plug, ausschalten_plug, lamp_plug_dict,
                                                    startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                                                    color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait)).start()
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']

                    
                    else:
                        current_ask_topic_sentence = random_satz_2 if current_ask_topic_sentence == random_satz_1 else random_satz_1
                        previous_state = states['ASK_TOPIC']  
                                          
                        if debug_mode == True: 
                            if i == 15: 
                                
                                server.server_output(conn, "Keine Signalwörter gefunden. Bitte versuch es nochmal.")
                            print("No matching signal words found.")
                            
            else:
                if debug_mode == True:
                    if i == 15: 
                        print("i=16 ")
                        server.server_output(conn, "Keine Signalwörter gefunden. Bitte versuch es nochmal.")
                    print("error No matching signal words found.")
                    

        except Exception as e:
            if debug_mode == True: print("chat_dialog" + f"Error: {e}")
            time.sleep(0.5)
            #funktions.text_to_speech(engine, pyttsx_voice_id, "unbekannte Wörter oder Problem. Bitte überleg mal woran es liegen könnte.")
            current_state = states['ASK_TOPIC']
            previous_state = states['ASK_TOPIC']  # Reset previous_state in case of an error

def server_input(conn):        
    server_input = server.get_server_input(conn)  
    #server.conn_close(conn)
    print(server_input)
    return server_input

# Voice Assistent Logik und Funktionsimplementierungen Ende
if __name__ == "__main__": 
    import server
    from vosk import Model, KaldiRecognizer
    import pyttsx3
    engine = pyttsx3.init()   
    pyttsx_voice_id = 0 
    if debug_mode == False: funktions.clear_voice_assistent()
    
    # Initialize Huggingface chatbot
    chatbot = funktions.initialize_huggingface()
    try:
        funktions.huggingface_newchat(chatbot)
    except Exception as e:
            if debug_mode == True: print("Huggingface: " + f"Error: {e}")   
    if debug_mode == False: funktions.clear_voice_assistent()
    
    chat_dialog_thread = threading.Thread(target=chat_dialog(engine))#, daemon=True, args=(engine, app)
    chat_dialog_thread.start()
    
    
    
    
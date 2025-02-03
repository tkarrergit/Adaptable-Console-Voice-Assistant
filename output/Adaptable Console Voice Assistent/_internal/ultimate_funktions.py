#Beleuchtung Anfang
from PyP100 import PyP100
from PyP100 import PyL530
import Tapo
import configparser
import funktions
import main
debug_mode = main.debug_mode

def ultimate_light(strahler_1, strahler_2, strahler_3, strahler_4, plug_1, plug_2, plug_3, plug_4, strahler_color_strobe_multi, strahler_color_fade_multi, strahler_slow_fade_out,
                   strahler_speed_fade_out, anschalten_strahler_multi_color, anschalten_strahler_2_4_color, anschalten_strahler_1_3_color,
                   anschalten_strahler_multi_licht, anschalten_strahler_2_4_licht, anschalten_strahler_1_3_licht, ausschalten_strahler, anschalten_plug_multi,
                   anschalten_plug_2_4, anschalten_plug_1_3, anschalten_plug_1, anschalten_plug_2_3_4, ausschalten_plug,
                   startfarbe_d1, brightness_d1, startfarbe_d2, brightness_d2, startfarbe_d3, brightness_d3, startfarbe_d4, brightness_d4,
                   color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait):

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
#Beleuchtung Ende
#Combinations Anfang

def ultimate_combination(user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
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
                        color_distanz, dimmzielwert, dimm_geschwindigkeit, brightness, farbton, saettigung, temp, wait):
    if debug_mode == True: print("Kombination")
    
    user_combination_inputs =[user_combination_input_1, user_combination_input_2, user_combination_input_3, user_combination_input_4, user_combination_input_5, user_combination_input_6, 
                         user_combination_input_7, user_combination_input_8, user_combination_input_9, user_combination_input_10]
    # Lese die INI-Datei
    config = configparser.ConfigParser()

    # Füge die Standard-Config hinzu
    config.read(funktions.resource_path('config/chat_config.ini'))

    # Pfade zu den weiteren Config-Dateien
    additional_config_paths = [
        funktions.resource_path('config/app_config.ini'),
        funktions.resource_path('config/tapo_config.ini'),
        funktions.resource_path('config/benutzer_settings_config.ini'),
        funktions.resource_path('config/combination_config.ini')
        # Füge hier die Pfade für die restlichen Config-Dateien hinzu
    ]

    # Füge die zusätzlichen Config-Dateien hinzu
    config.read(additional_config_paths)
    
    for user_combination_input in user_combination_inputs:        
        
        if user_combination_input:          
            for i in range(1, 16):

                    # ChatSettings Config
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
                    keys_1_list = main.ast.literal_eval(f"[{keys_1_str}]")
                    keys_2_str = config.get(app_section_name, 'keys_2')
                    keys_2_list = main.ast.literal_eval(f"[{keys_2_str}]")
                    keys_3_str = config.get(app_section_name, 'keys_3')
                    keys_3_list = main.ast.literal_eval(f"[{keys_3_str}]")
                    keys_4_str = config.get(app_section_name, 'keys_4')
                    keys_4_list = main.ast.literal_eval(f"[{keys_4_str}]")
                    keys_5_str = config.get(app_section_name, 'keys_5')
                    keys_5_list = main.ast.literal_eval(f"[{keys_5_str}]")
                    keys_6_str = config.get(app_section_name, 'keys_6')
                    keys_6_list = main.ast.literal_eval(f"[{keys_6_str}]")
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

                    if user_input_enabled:
                        user_input_i = user_input + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    else:
                        user_input_i = user_input_task + " " + user_input_context + " " + user_input_example + " " + user_input_persona + " " + user_input_format + " " + user_input_tone

                    user_input = user_combination_input
                    if funktions.contains_signal_word(user_input, signal_words, and_signal_words, section_name):
                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "ok")
                        if debug_mode == False:funktions.clear_voice_assistent()
                        Signal_word_found = True
                        if dialog_chat_enabled:
                            funktions.print_center_zeile("Dialogmodus wird gestartet. Einen kleinen Augenblick bitte.", 1, "left")
                            funktions.huggingface_newchat(main.chatbot)
                            while True:
                                funktions.print_center_zeile("Dialogmodus                                                                         ", 1, "left")
                                funktions.process_user_input(main.engine, active_chat_engine, user_input_i, main.chatbot, main.pyttsx_voice_id)
                                if debug_mode == True: print("process_user_input fertiggestellt")
                                user_input_i = funktions.get_user_input(main.vosk_recognizer)
                                if debug_mode == True: print("user_input_i: " + user_input_i)
                                if "abbruch" in user_input_i.lower() or "stopp" in user_input_i.lower() or "es reicht" in user_input_i.lower() or "stop" in user_input_i.lower() or "parar" in user_input_i.lower():
                                    if funktions.pyttsx_voice_id == 0:
                                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "Danke, war ein gutes Gespräch")
                                    elif funktions.pyttsx_voice_id == 2:
                                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "Ok, thank you for the nice conversation")
                                    elif funktions.pyttsx_voice_id == 4:
                                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "Sie claro, gracias por la buen conversación")
                                    if debug_mode == False:funktions.clear_voice_assistent()                                    
                                    current_ask_topic_sentence = main.random_satz_2 if current_ask_topic_sentence == main.random_satz_1 else main.random_satz_1
                                    previous_state = main.states['ASK_TOPIC']
                                    break
                        else:                                                                                
                            funktions.process_user_input(main.engine, active_chat_engine, user_input_i, main.chatbot, main.pyttsx_voice_id)
                            current_ask_topic_sentence = main.random_satz_2 if current_ask_topic_sentence == main.random_satz_1 else main.random_satz_1
                            previous_state = main.states['ASK_TOPIC']
                            break

                    elif funktions.app_contains_signal_word(user_input, app_signal_words, app_and_signal_words, app_section_name):
                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "ok")
                        Signal_word_found = True
                        if debug_mode == True: print("App Funktion")
                        user_input_app = funktions.input_app(user_input, app_signal_words, app_and_signal_words)
                        if debug_mode == True:print(user_input_app)
                        funktions.app_ultimate(app, hotkey_1_tup, hotkey_2_tup, hotkey_3_tup, hotkey_4_tup, hotkey_5_tup, hotkey_6_tup, wait_app,
                                    wait_1_1, wait_1_2, wait_1_3, wait_2_1, wait_2_2, wait_2_3, 
                                    wait_3_1, wait_3_2, wait_3_3, wait_4_1, wait_4_2, wait_4_3,
                                    wait_5_1, wait_5_2, wait_5_3, wait_6_1, wait_6_2, wait_6_3,
                                    text_1, text_2, text_3, text_4, text_5, text_6, keys_1_list,
                                    keys_2_list, keys_3_list, keys_4_list, keys_5_list, keys_6_list,
                                    user_input_enabled_1, user_input_enabled_2, user_input_enabled_3,
                                    user_input_enabled_4, user_input_enabled_5, user_input_enabled_6,
                                    user_input_app)
                        previous_state = main.states['ASK_TOPIC']
                        break
                        
                    elif funktions.tapo_contains_signal_word(user_input, tapo_signal_words, tapo_and_signal_words, tapo_section_name):
                        funktions.text_to_speech(main.engine, main.pyttsx_voice_id, "ok")
                        Signal_word_found = True
                        Tapo.anmelden(strahler_1, strahler_2, strahler_3, strahler_4)
                        
                        main.threading.Thread(target=ultimate_light, daemon=True, args=(
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
                        current_ask_topic_sentence = main.random_satz_2 if current_ask_topic_sentence == main.random_satz_1 else main.random_satz_1
                        previous_state = main.states['ASK_TOPIC']

        else:            
            break    

#Combinations Ende
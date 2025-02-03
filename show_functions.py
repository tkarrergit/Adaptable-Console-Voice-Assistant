import time
import os

from variables_for_all import debug_mode
from variables_for_all import pyttsx_voice_id



class ConsoleColors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'

def colorize_signal_words(sentence_start, sentence_end, word, and_word, function_description, color=ConsoleColors.RESET):
    
    text_1 = f"{sentence_start} {color}{word}{ConsoleColors.RESET} {color}{and_word}{ConsoleColors.RESET} {sentence_end} {function_description}"  
        
    return text_1
    

def scroll_colored_text_bottom(text, color=ConsoleColors.RESET, speed=0.1):
    # Textlänge berechnen
    text_length = len(text)
    
    # Breite und Höhe der Konsole abrufen
    console_width, console_height = os.get_terminal_size()

    # Leerer Raum vor dem Text hinzufügen, um Platz am rechten Rand zu schaffen
    text = ' ' * (console_width - text_length) + text
    # Anzahl der Schritte für den Scroll-Effekt berechnen
    steps = max(console_width + 1, 1)
    
    # Endlose Schleife für den Scroll-Effekt
    while True:
        
        steps -= 1
        if steps > 0:
            # Text am unteren Rand der Konsole anzeigen
            print('\033[{};1H'.format(console_height-1))  # Setze den Cursor auf die unterste Zeile
            print(f"{color}{text}{ConsoleColors.RESET}", end='\r')

            # Text um einen Schritt nach links verschieben
            text = text[1:] + " "

            # Kurze Verzögerung für den Scroll-Effekt
            time.sleep(speed)
        else:
            break

import random
import time
import shutil



import ctypes  
class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

def anzeigen_und_ausblenden_old(text_1, text_2, text_3, speed=5):
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

    # Set console cursor position for text_1
    ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_3)

    # Einblenden text_1
    print(text_3, end='\r')

    time.sleep(2)  # 5 Sekunden anzeigen lassen

    # Ausblenden text_1
    print(' ' * terminal_breite, end='\r')

    # Koordinaten reset
    ctypes.windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))

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

    # Set console cursor position for text_1
    ctypes.windll.kernel32.SetConsoleCursorPosition(h, position_2)

    # Einblenden text_1
    print(text_2, end='\r')

    time.sleep(speed)  # 5 Sekunden anzeigen lassen

    # Ausblenden text_1
    print(' ' * terminal_breite, end='\r')

    # Koordinaten reset
    ctypes.windll.kernel32.SetConsoleCursorPosition(h, COORD(0, 0))




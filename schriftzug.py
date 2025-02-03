#!/usr/bin/env python3
import threading
from asciimatics.renderers import FigletText, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.effects import Print
from asciimatics.exceptions import ResizeScreenError
from pyfiglet import Figlet
import sys
import pyautogui
import time


def demo(screen):
    scenes = []

    

    text = Figlet(font="banner", width=1800).renderText("Hallo du  dss")
    width = max([len(x) for x in text.split("\n")])

    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 40, screen.colours),
              0,
              speed=1,
              transparent=False),
        Print(screen,
              FigletText("Console Voice Assistant", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_BLACK,
              bg=Screen.COLOUR_BLACK,
              speed=1),
        Print(screen,
              FigletText("Console Voice Assistant", "banner"),
              screen.height - 9,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)

def Schriftzug():
    
    while True:
        try:
            Screen.wrapper(demo)
            sys.exit(0)            
        except ResizeScreenError:
            pass


def call_schriftzug_thread():
    global schriftzug_thread     
    schriftzug_thread = threading.Thread(target=Schriftzug)
    schriftzug_thread.start()

def stop_schriftzug_thread():
    
    pyautogui.key("q")
                  
     
#if __name__ == "__main__":
    #call_schriftzug_thread()
    #stop_schriftzug_thread()
    
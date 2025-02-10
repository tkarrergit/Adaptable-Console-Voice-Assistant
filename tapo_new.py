


from PyP100 import PyP100
from PyP100 import PyL530
import time


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


def anschalten_lampe_color(*lamps, brightness=brightness, farbton=farbton, saettigung=saettigung):
    print("HHHHanschalten_lampe_color: ", brightness, farbton, saettigung)
    
    for lamp in lamps:
        lamp.turnOn()
        lamp.setColor(farbton, saettigung)
        lamp.setBrightness(brightness)
    	
    	
def anschalten_lamp_temp(*lamps, brightness, temp):
    
    for lamp in lamps:
        lamp.turnOn()
        lamp.setBrightness(brightness)
        lamp.setColorTemp(temp)
    	
    	

def ausschalten_lamp(*lamps):
    
    for lamp in lamps:
    	lamp.turnOff()
    	
    	
def anschalten_lamp(*lamps):
    
    for lamp in lamps:
    	lamp.turnOn()
    	
    	
def anschalten_plug(*plugs):
	
	for plug in plugs:
		plug.turnOn()
		
		
def ausschalten_plug(*plugs):
	
	for plug in plugs:
		plug.turnOff()
		
		
def strahler_slow_fade_out(*lamps, dimmzielwert, dimm_geschwindigkeit, brightness):
    global halb_zaehler, viertel_zaehler
    halb_zaehler = 0
    viertel_zaehler = 0
    bereich = abs(brightness - dimmzielwert)                            # B 100 - D 20= 80
    schritte = int(bereich / 3)                                     # 80 : 4 = 20
    schritte_bereinigt = schritte + 2                               # 20 + 1 = 21
    viertel_schritte = int(schritte_bereinigt / 4)                  # 21 : 4 = 5,25
    print("viertel_schritte = " + str(viertel_schritte))
    hälfte_schritte = int(schritte_bereinigt / 2)                   # 21 : 2 = 10,5
    print("halb_schritte = " + str(hälfte_schritte))
    try:
        if 0 <= dimmzielwert <= 100:
            for lampe in lamps:
                lampe.setBrightness(brightness)       
            
            while schritte_bereinigt >= 1:
                if schritte_bereinigt > hälfte_schritte:
                    print("größer hälfte")
                    brightness = brightness - 3
                    
                    for lampe in lamps:
                        lampe.setBrightness(brightness)            			
                        print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    
                    schritte_bereinigt = schritte_bereinigt - 1
                    print(schritte_bereinigt)
                elif schritte_bereinigt > viertel_schritte:
                    print("größer viertel")
                    brightness = brightness - 2

                    for lampe in lamps:
                        lampe.setBrightness(brightness)                 
                        print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    
                    time.sleep(dimm_geschwindigkeit)

                    if halb_zaehler > abs(viertel_schritte/3):            # 5,25 : 3 =
                        schritte_bereinigt = schritte_bereinigt - 1
                        print(schritte_bereinigt)
                    else:
                        halb_zaehler = halb_zaehler + 1
                        print(halb_zaehler)
                else:
                    brightness = brightness - 1
                    for lampe in lamps:
                        lampe.setBrightness(brightness)
                        print(f"{str(lampe)} gedimmt auf Helligkeit: {brightness}")
                    time.sleep(abs(dimm_geschwindigkeit))
                    if dimmzielwert == 0 and brightness <= 1:
                        time.sleep(1)
                        for lampe in lamps:
                            ausschalten_lamp(lampe)
                        
                    elif viertel_zaehler > abs((viertel_schritte / 3)*5.4):
                        schritte_bereinigt = schritte_bereinigt - 1
                        print(schritte_bereinigt)
                    else:
                        viertel_zaehler = viertel_zaehler + 1
                        print(viertel_zaehler)

        else:
            print("Ungültige Eingabewerte. Dimmwert muss im Bereich von 0 bis 100 liegen, und Geschwindigkeit muss eine positive Zahl sein.")

    except Exception as e:
            print(f"Error: {e}")
from PyP100 import PyP100
from PyP100 import PyL530
import time

s_ip_1 = "192.168.68.115"
s_ip_2 = "192.168.68.148"
s_ip_3 = "192.168.68.147"
s_ip_4 = "192.168.68.146"
p_ip_1 = "192.168.68.143"
p_ip_2 = "192.168.68.144"
p_ip_3 = "192.168.68.145"
p_ip_4 = "192.168.68.142"
e_mail = "sandburg.registrierung@mail.de"
passwort = "Heckmeck16!"

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



strahler_1 = PyL530.L530(s_ip_1, e_mail, passwort)
strahler_2 = PyL530.L530(s_ip_2, e_mail, passwort)
strahler_3 = PyL530.L530(s_ip_3, e_mail, passwort)
strahler_4 = PyL530.L530(s_ip_4, e_mail, passwort)

plug_1 = PyP100.P100(p_ip_1, e_mail, passwort)
plug_2 = PyP100.P100(p_ip_2, e_mail, passwort)
plug_3 = PyP100.P100(p_ip_3, e_mail, passwort)
plug_4 = PyP100.P100(p_ip_4, e_mail, passwort)

#Grundfunktionen zum Erstellen anderer Funktionen Anfang

def anmelden(strahler_1, strahler_2, strahler_3, strahler_4):
    devices = [strahler_1, strahler_2, strahler_3, strahler_4]
    try:
        for device in devices:
            device.handshake()
            device.login()

        print("angemeldet")
    except Exception as e:
            print(f"Error: {e}")

def anschalten(device):
    device.turnOn()
    print(str(device) + " an")

def ausschalten(device):
    device.turnOff()
    print(str(device) + " aus")

def toggle_state(device):
    device.toggleState()
    print(str(device) + " geschaltet")

def getDeviceInfo(device):
    device_info = device.getDeviceInfo()
    print(device_info)

def update_brightness(device):
    global device_info  # 'global' wird verwendet, um auf die globale Variable zuzugreifen
    device_info = device.getDeviceInfo()
    # Den Wert hinter 'brightness' auslesen und in einer Variable speichern
    brightness_update = device_info['brightness']
    print(brightness_update)
    return brightness_update

def getDeviceName(device):
    device_name = device.getDeviceName()
    print(device_name)

def setBrightness(device):
    device.setBrightness(brightness)
    print(str(device) + ": " + "Helligkeit: " + str(brightness))

def setColorTemp(device):
    device.setColorTemp(temp)
    print(str(device) + ": " + "Farbtemperatur: " + str(temp))


def setColor(device):
    device.setColor(farbton, saettigung)
    print(str(device) + ": " + "Farbton: " + str(farbton) + " Sättigung: " + str(saettigung))


def showAllColors(device):
    # Annahme: Farbton im Bereich von 0 bis 359, Sättigung im Bereich von 0 bis 100
    try:
        for hue in range(0, 360, 1):  # Schritte von 10
            device.setColor(hue, 100)
            time.sleep(0)
            print(f"{str(device)}: Farbton={hue}, Sättigung={100}")
    except Exception as e:
            print(f"Error: {e}")

#Grundfunktionen zum Erstellen anderer Funktionen Anfang

#Effekte und Funktionen für Strahler Anfang

def strahler_color_fade_multi(device_1, startfarbe_d1, brightness_d1, device_2, startfarbe_d2, brightness_d2, device_3, startfarbe_d3, brightness_d3, device_4, startfarbe_d4, brightness_d4, color_distanz, wait):
    device_1.setBrightness(brightness_d1)
    device_2.setBrightness(brightness_d2)
    device_3.setBrightness(brightness_d3)
    device_4.setBrightness(brightness_d4)
    color_d1 = startfarbe_d1
    color_d2 = startfarbe_d2
    color_d3 = startfarbe_d3
    color_d4 = startfarbe_d4
    try:
        while True:
            device_1.setColor(color_d1, 100)
            device_2.setColor(color_d2, 100)
            device_3.setColor(color_d3, 100)
            device_4.setColor(color_d4, 100)
            color_d1 = color_d1 + color_distanz
            color_d3 = color_d3 + color_distanz
            color_d2 = color_d2 + color_distanz
            color_d4 = color_d4 + color_distanz
            time.sleep(wait)
            if color_d1 >= 360:
                color_d1 = 0
            elif color_d2 >= 360:
                color_d2 = 0
            elif color_d3 >= 360:
                color_d3 = 0
            elif color_d4 >= 360:
                color_d4 = 0

    except Exception as e:
        print(f"Error: {e}")


def strahler_color_strobe_multi(device_1, startfarbe_d1, brightness_d1, device_2, startfarbe_d2, brightness_d2, device_3, startfarbe_d3, brightness_d3, device_4, startfarbe_d4, brightness_d4, color_distanz, wait):
    device_1.setBrightness(brightness_d1)
    device_2.setBrightness(brightness_d2)
    device_3.setBrightness(brightness_d3)
    device_4.setBrightness(brightness_d4)
    color_d1 = startfarbe_d1
    color_d2 = startfarbe_d2
    color_d3 = startfarbe_d3
    color_d4 = startfarbe_d4
    zahl = 0
    disco = True
    try:
        while disco == True:
            print(zahl)
            if zahl % 2 == 0:
                device_3.setBrightness(brightness_d3)
                device_4.setBrightness(1)
                device_1.setBrightness(brightness_d1)
                device_2.setBrightness(1)
                device_3.setColor(color_d3, 100)
                device_1.setColor(color_d1, 100)
                color_d1 = color_d1 + color_distanz
                color_d3 = color_d3 + color_distanz
                time.sleep(wait)
                if color_d1 >= 360:
                    color_d1 = 0
                elif color_d3 >= 360:
                    color_d3 = 0
            else:
                device_1.setBrightness(1)
                device_2.setBrightness(brightness_d2)
                device_3.setBrightness(1)
                device_4.setBrightness(brightness_d4)
                device_2.setColor(color_d2, 100)
                device_4.setColor(color_d4, 100)
                color_d2 = color_d2 + color_distanz
                color_d4 = color_d4 + color_distanz
                time.sleep(wait)
                if color_d2 >= 360:
                    color_d2 = 0
                elif color_d4 >= 360:
                    color_d4 = 0
            zahl += 1
            if zahl >= 10:
                disco = False


    except Exception as e:
        print(f"Error: {e}")

    anschalten_strahler_multi_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp)

def strahler_speed_fade_out(device_1, device_2, device_3, device_4, dimmzielwert, dimm_geschwindigkeit, brightness):
    global halb_zaehler, viertel_zaehler
    halb_zaehler = 0
    viertel_zaehler = 0
    try:
        if 0 <= dimmzielwert <= 100:
            device_1.setBrightness(brightness)
            device_2.setBrightness(brightness)
            device_3.setBrightness(brightness)
            device_4.setBrightness(brightness)
            bereich = abs(brightness - dimmzielwert)  # B 100 - D 20= 80
            schritte = int(bereich / 3)  # 80 : 4 = 20
            schritte_bereinigt = schritte  # 20 + 1 = 21
            viertel_schritte = int(schritte_bereinigt / 4)  # 21 : 4 = 5,25
            print("viertel_schritte = " + str(viertel_schritte))
            hälfte_schritte = int(schritte_bereinigt / 2)  # 21 : 2 = 10,5
            print("halb_schritte = " + str(hälfte_schritte))

            while schritte_bereinigt >= 1:
                brightness = brightness - 3
                device_1.setBrightness(brightness)
                device_2.setBrightness(brightness)
                device_3.setBrightness(brightness)
                device_4.setBrightness(brightness)
                print(f"{str(device_1)} gedimmt auf Helligkeit: {brightness}")
                schritte_bereinigt = schritte_bereinigt - 1
                print(schritte_bereinigt)
                time.sleep(dimm_geschwindigkeit)
                if dimmzielwert == 0 and brightness <= 2:
                    time.sleep(1)
                    ausschalten(strahler_1)
                    ausschalten(strahler_2)
                    ausschalten(strahler_3)
                    ausschalten(strahler_4)

        else:
            print(
                "Ungültige Eingabewerte. Dimmwert muss im Bereich von 0 bis 100 liegen, und Geschwindigkeit muss eine positive Zahl sein.")
    except Exception as e:
        print(f"Error: {e}")

def strahler_slow_fade_out(device_1, device_2, device_3, device_4, dimmzielwert, dimm_geschwindigkeit, brightness):
    global halb_zaehler, viertel_zaehler
    halb_zaehler = 0
    viertel_zaehler = 0
    try:
        if 0 <= dimmzielwert <= 100:
            device_1.setBrightness(brightness)
            device_2.setBrightness(brightness)
            device_3.setBrightness(brightness)
            device_4.setBrightness(brightness)
            bereich = abs(brightness - dimmzielwert)                            # B 100 - D 20= 80
            schritte = int(bereich / 3)                                     # 80 : 4 = 20
            schritte_bereinigt = schritte + 2                               # 20 + 1 = 21
            viertel_schritte = int(schritte_bereinigt / 4)                  # 21 : 4 = 5,25
            print("viertel_schritte = " + str(viertel_schritte))
            hälfte_schritte = int(schritte_bereinigt / 2)                   # 21 : 2 = 10,5
            print("halb_schritte = " + str(hälfte_schritte))


            while schritte_bereinigt >= 1:
                if schritte_bereinigt > hälfte_schritte:
                    print("größer hälfte")
                    brightness = brightness - 3
                    device_1.setBrightness(brightness)
                    device_2.setBrightness(brightness)
                    device_3.setBrightness(brightness)
                    device_4.setBrightness(brightness)
                    print(f"{str(device_1)} gedimmt auf Helligkeit: {brightness}")
                    schritte_bereinigt = schritte_bereinigt - 1
                    print(schritte_bereinigt)
                elif schritte_bereinigt > viertel_schritte:
                    print("größer viertel")
                    brightness = brightness - 2
                    device_1.setBrightness(brightness)
                    device_2.setBrightness(brightness)
                    device_3.setBrightness(brightness)
                    device_4.setBrightness(brightness)
                    print(f"{str(device_1)} gedimmt auf Helligkeit: {brightness}")
                    time.sleep(dimm_geschwindigkeit)
                    if halb_zaehler > abs(viertel_schritte/3):            # 5,25 : 3 =
                        schritte_bereinigt = schritte_bereinigt - 1
                        print(schritte_bereinigt)
                    else:
                        halb_zaehler = halb_zaehler + 1
                        print(halb_zaehler)
                else:
                    brightness = brightness - 1
                    device_1.setBrightness(brightness)
                    device_2.setBrightness(brightness)
                    device_3.setBrightness(brightness)
                    device_4.setBrightness(brightness)
                    print(f"{str(device_1)} gedimmt auf Helligkeit: {brightness}")
                    time.sleep(abs(dimm_geschwindigkeit))
                    if dimmzielwert == 0 and brightness <= 1:
                        time.sleep(1)
                        ausschalten(strahler_1)
                        ausschalten(strahler_2)
                        ausschalten(strahler_3)
                        ausschalten(strahler_4)
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

def anschalten_strahler_multi_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung):
    strahler_1.turnOn()
    strahler_1.setColor(farbton, saettigung)
    strahler_1.setBrightness(brightness)
    strahler_2.turnOn()
    strahler_2.setColor(farbton, saettigung)
    strahler_2.setBrightness(brightness)
    strahler_3.turnOn()
    strahler_3.setColor(farbton, saettigung)
    strahler_3.setBrightness(brightness)
    strahler_4.turnOn()
    strahler_4.setColor(farbton, saettigung)
    strahler_4.setBrightness(brightness)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def anschalten_strahler_2_4_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung):
    strahler_2.turnOn()
    strahler_2.setColor(farbton, saettigung)
    strahler_2.setBrightness(brightness)
    strahler_4.turnOn()
    strahler_4.setColor(farbton, saettigung)
    strahler_4.setBrightness(brightness)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def anschalten_strahler_1_3_color(strahler_1, strahler_2, strahler_3, strahler_4, brightness, farbton, saettigung):
    strahler_1.turnOn()
    strahler_1.setColor(farbton, saettigung)
    strahler_1.setBrightness(brightness)
    strahler_3.turnOn()
    strahler_3.setColor(farbton, saettigung)
    strahler_3.setBrightness(brightness)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def anschalten_strahler_multi_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp):
    strahler_1.turnOn()
    strahler_1.setBrightness(brightness)
    strahler_1.setColorTemp(temp)
    strahler_2.turnOn()
    strahler_2.setBrightness(brightness)
    strahler_2.setColorTemp(temp)
    strahler_3.turnOn()
    strahler_3.setBrightness(brightness)
    strahler_3.setColorTemp(temp)
    strahler_4.turnOn()
    strahler_4.setBrightness(brightness)
    strahler_4.setColorTemp(temp)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def anschalten_strahler_2_4_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp):
    strahler_2.turnOn()
    strahler_2.setBrightness(brightness)
    strahler_2.setColorTemp(temp)
    strahler_4.turnOn()
    strahler_4.setBrightness(brightness)
    strahler_4.setColorTemp(temp)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def anschalten_strahler_1_3_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp):
    strahler_1.turnOn()
    strahler_1.setBrightness(brightness)
    strahler_1.setColorTemp(temp)
    strahler_3.turnOn()
    strahler_3.setBrightness(brightness)
    strahler_3.setColorTemp(temp)
    devices = [strahler_1, strahler_2, strahler_2, strahler_2]
    print(str(devices) + " an")

def ausschalten_strahler(strahler_1, strahler_2, strahler_3, strahler_4):
    strahler_4.turnOff()
    strahler_3.turnOff()
    strahler_2.turnOff()
    strahler_1.turnOff()

def anschalten_strahler_1(strahler_1):
    
    strahler_1.turnOn()

def ausschalten_strahler_1(strahler_1):
    
    strahler_1.turnOff()
#Effekte und Funktionen für Strahler Ende

#Funktionen für Plug´s Anfang
def anschalten_plug_multi(plug_1, plug_2, plug_3, plug_4):
    plug_4.turnOn()
    plug_3.turnOn()
    plug_2.turnOn()
    plug_1.turnOn()

def anschalten_plug_2_4(plug_2, plug_4):
    plug_2.turnOn()
    plug_4.turnOn()

def anschalten_plug_1_3(plug_1, plug_3):
    plug_1.turnOn()
    plug_3.turnOn()

def anschalten_plug_1(plug_1):
    plug_1.turnOn()


def anschalten_plug_2_3_4(plug_2, plug_3, plug_4):
    plug_2.turnOn()
    plug_3.turnOn()
    plug_4.turnOn()

def ausschalten_plug(plug_1, plug_2, plug_3, plug_4):
    plug_4.turnOff()
    plug_3.turnOff()
    plug_2.turnOff()
    plug_1.turnOff()

def ausschalten_plug_2( plug_2):
    
    plug_2.turnOff()
    
#Funktionen für Plug´s Ende




def licht_show(device):
    #brightness_update = update_brightness(strahler_1)
    #brightness = brightness_update
    #anmelden(device, device)
    #getDeviceName(device)
    #anschalten_strahler_multi_licht(strahler_1, strahler_2, strahler_3, strahler_4, brightness, temp)
    #anschalten(device)
    #color_fade_multi(strahler_1, 0, strahler_2, 0, strahler_3, 0, strahler_4, 0, 10, 1)
    #slow_fade_out(strahler_1, strahler_2, strahler_3, strahler_4, dimmzielwert, dimm_geschwindigkeit, brightness)
    #slow_fade_out(strahler_1, strahler_2, strahler_3, strahler_4, dimmzielwert, dimm_geschwindigkeit, brightness)
    #setBrightness(device)
    #showAllColors(device)
    anmelden(strahler_1, strahler_2, strahler_3, strahler_4)
    anschalten_strahler_1(strahler_1)
    #anschalten_plug_1(plug_2)
    time.sleep(7)
    #ausschalten_plug_2(plug_2)
    ausschalten_strahler_1(strahler_1)





if __name__ == "__main__":
    pass
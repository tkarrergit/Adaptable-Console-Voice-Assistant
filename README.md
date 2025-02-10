# Adaptable Console Voice Assistant

**Status:** 
Early Development / Beta Features / It's actually out of order!

**Entwicklungszeitraum:** 
		November, 2023 bis März, 2024
  
⚠️ **Achtung:** Bei der Nutzung von Hugging Chat kann es gerade zu folgenden serverseitigen Störungen kommen:
- Fehler "Model overloaded"
- Langsame Antworten durch volle Server
- Chat bricht manchmal ab
  
**Technologien**:
- **Python**: Hauptprogrammiersprache für die flexible und leistungsstarke Implementierung.
- **PyAutoGUI**: Automatisierung von Benutzerinteraktionen und App-Steuerung.
- **PyP100**: Steuerung und Automatisierung von Tapo-Lampen und Smart-Geräten.
- **HugChat**: Integration moderner Sprachmodelle über die Soulter-API.
- **Vosk**: Offline-Spracherkennung für schnelle und datenschutzfreundliche Sprachverarbeitung.
- **pyttsx3**: Offline-Sprachausgabe für ressourcenschonende Wiedergabe.

---

## Projektbeschreibung

**Kurzbeschreibung**:

Der **Adaptable Console Voice Assistant "Paul"** ist ein vielseitiger Sprachassistent für die Konsole.
- **Hauptfunktionen**: 
  - **Chat- und LLM-Funktionen**,
  - **Beleuchtungssteuerung für Tapo-Lampen** 
  - und **App-Steuerung**. 

- "Paul" kann auch mehrerer Funktionen kombinieren: Beispielsweise dimmt Paul das Licht, startet eine Playlist und erzählt gleichzeitig eine Geschichte.
- Alle Funktionen lassen sich flexibel über individuelle Config-Dateien konfigurieren. Der Kreativität sind wenig Grenzen gesetzt.

- Dank offline Spracherkennung (Vosk) und Sprachausgabe (pyttsx3) ist der Assistent Datenschutz freundlich und ressourcenschonend. 

- Mit HuggingChat bleibt die Nutzung zukunftssicher durch vielfältige Open-Source-Modelle.

## Motivation
Dieses Projekt war mein Einstieg in Python und wurde von mir entwickelt, da ich Sprachassistenten ungeheuer faszinierend finde und die Vorstellung, dies selbst zu verwirklichen, eine tolle und unglaublich motivierende Vision für mich war. Realisiert habe ich dies durch die Kooperation mit einem Sprachmodell, viel Experimentierfreude und Durchhaltevermögen.

---
## Lernfortschritte 

**Persönliche Erkenntnisse:**
- Ich habe ein solides Verständnis für die Grundlagen von Python gewonnen, einschließlich Funktionen, Schleifen, Datentypen und Operatoren.
- Mir wurde bewusst, wie wichtig es ist, die Anzahl externer Bibliotheken möglichst gering zu halten, um Komplikationen durch zukünftige Updates zu vermeiden.
- Die Integration von Sprachmodellen über HuggingChat hat mir gezeigt, wie flexibel moderne Sprachmodelle eingebunden werden können.
- Ich habe gelernt, wie nützlich Config-Dateien sind, um Funktionen individuell anzupassen und flexibel zu steuern.
- Darüber hinaus kam jedoch auch der Wunsch nach einer Datenbanklösung zur dynamischen Verwaltung und Erstellung von Funktionen auf.
- Durch die Nutzung von PyAutoGUI habe ich erste Erfahrungen in der Automatisierung von Anwendungen gesammelt.
- Die hohe Geschwindigkeit und Stabilität der offline Spracherkennung mit Vosk hat mich beeindruckt und mir gezeigt, dass Offline-Lösungen oft Datenschutz- und Geschwindigkeitsvorteile bieten.
- LLMs haben sich als wertvolle Informationsquelle erwiesen. Gleichzeitig habe ich festgestellt, dass ihre Grenzen recht schnell erreicht sind und eigene Entwicklungsarbeit notwendig machen.


---
## Features
**Aktuelle Funktionen:**
- **Nutzeransprache**: Aktiviert durch den Namen „Paul“ und individuelle Signalwörter.
- **Kommunikationsfunktionen**: Chat- und LLM-Interaktion für vielseitige Dialoge und dynamische Inhalte.
- **Smart-Home-Steuerung**: Beleuchtungssteuerung für Tapo-Lampen, einschließlich Dimmen, Farbwechsel und Gruppensteuerung.
- **Anwendungssteuerung**: Start und Steuerung externer Anwendungen, z. B. Musik- und Videoplayer.
- **Kombinationsmodi**: Verknüpfung mehrerer Funktionen, etwa synchronisierte Licht- und Mediensteuerung mit Sprachinhalten.
- **Flexible Konfiguration**: Individuelle Anpassung aller Funktionen durch Config-Dateien.


## Zukünftige Entwicklungen (Optional)
- **Grafische Benutzeroberfläche**: Entwicklung einer intuitiven und benutzerfreundlichen Visualisierung für einfache Steuerung und Konfiguration.
- **Datenbankintegration**: Ablösung der Config-Dateien durch eine leistungsfähige Datenbanklösung zur dynamischen Verwaltung und Erstellung von Funktionen.
- **Projektstrukturierung**: Überarbeitung der Architektur für bessere Skalierbarkeit, Wartbarkeit und Erweiterbarkeit des Projekts.


# myLLM1 

ist eine einfache Desktop-Anwendung zur Übersetzung kurzer Texte mit Hilfe der Google Gemini API. Die Übersetzung wird direkt im Programmfenster angezeigt, kann dort bearbeitet und anschließend als Excel-Datei gespeichert werden.

## Funktionen
- Texteingabe direkt im Programm (maximal 150 Wörter)

- Auswahl der Zielsprache über eine Auswahlliste (Englisch, Deutsch, Russisch, Aserbaidschanisch)

- Übersetzung erfolgt automatisch mit der Gemini-API

- Die Übersetzung kann vor dem Speichern bearbeitet werden

- Speicherung der Original- und Zieltexte in einer Excel-Datei mit dem Namen output.xlsx

## Voraussetzungen
Installiere die benötigten Python-Pakete mit folgendem Befehl im Terminal:

*pip install -r requirements.txt*

## API-Key
Für die Nutzung ist ein Google Gemini API-Key erforderlich.

Du kannst ihn auf zwei Arten bereitstellen:

1. Direkt im Programmfenster eingeben

2. Oder in einer Datei mit dem Namen gemini_api_key.txt speichern. Diese Datei muss sich im gleichen Ordner wie das Programm befinden und darf nur eine Zeile enthalten – deinen API-Key.

Beispiel für den Inhalt der Datei:

*AIzaSyD...deinKey*

> **WICHTIG**: Diese Datei darf niemals öffentlich hochgeladen werden, z. B. auf GitHub.

## Start
Starte das Programm im Terminal oder über PyCharm mit diesem Befehl:

*python myLLm1.py*

## Ergebnis
Nach der Übersetzung wird automatisch eine Datei mit dem Namen output.xlsx im Projektordner erstellt. Darin stehen:

*In der Spalte "input": der eingegebene Text*

*In der Spalte "output": die bearbeitete Übersetzung*
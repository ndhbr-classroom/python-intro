# Aufgabe 1: Intro
In dieser Aufgabe wirst du dein erstes Python-Programm programmieren und ausführen.

## Schritt 1: Der Dateien-Jungle
Du bist bestimmt durch die ganzen Dateien erst einmal verwirrt und überfordert. Aber es ist alles einfacher als du denkst.

Im Laufe dieses Kurses wirst du den Sinn der jeweiligen Dateien noch früh genug kennenlernen. Doch in dieser Aufgabe musst du dich erstmal nur mit der Datei **name.py** beschäftigen.

## Schritt 2: Ausführung
Nun geht's an die Ausführung. Wie bereits vorher erwähnt, existieren bereits einige Dateien, die dir den Einstieg erleichtern. Diese bilden die Grundstruktur des Programms.

Das Ziel des Programms ist es, dass das Programm dich nach deinem Namen frägt und es diesen in folgender Form wieder ausgibt.

```bash
Wie ist dein Name? Andreas
Hallo, mein Name ist Andreas!
```

Um das Programm auszuführen, solltest du in der Shell folgenden Befehl ausführen:
```bash
python main.py
```

Lass mich raten, du wirst bereits nach deinem Namen gefragt, aber nach Drücken der Enter-Taste beendet sich das Programm einfach?

Richtig, das ist deine Aufgabe!

## Schritt 3: Aufgabe
Das Programm frägt dich bereits nach deinem Namen. Nun ist es deine Aufgabe, dass das Programm den vorher erwähnten Satz wieder ausgibt.

Hierfür musst du die Datei **name.py** öffnen. Die Dateiendung **.py** steht im Übrigen für die Programmiersprache Python.

In Python kann man beispielsweise mit dem Zeichen **#** einen Kommentar erstellen. Alles was hinter diesen Zeichen steht, wird ignoriert. Dies ist hilfreich, um geschriebenen Code zu erklären.

Ersetze den Kommentar (Zeile 2) in der Funktion **print_name** mit folgendem Code:

```python
    print("Hallo, mein Name ist " + name)
```

Der Befehl **print(...)** gibt Text in der Konsole aus. In diesem Beispiel haben wir zwei Zeichenfolgen (auch: Strings) miteinander konkatiniert.

>Achtung! Damit dein eingesetzter Code wirklich Teil der Funktion **print_name** ist, muss die Zeile eingerückt sein (1x Tabulator-Taste).

## Schritt 4: Ausprobieren
Glückwunsch, das war's.

Wenn alles geklappt hat, ist die Aufgabe nun bereit zum abgeben. Teste sie doch gleich aus. Die Prozedur ist dieselbe. Starte die Anwendung mit:
```bash
python main.py
```
und probier es doch mit deinem Namen aus! :)

## Lösung
<details>
  <summary>Nur aufklappen, wenn du wirklich Hilfe brauchst! Probiere es zuerst ohne Lösung.</summary>
  
  ### loop.py
  ```python
        print(f'Hallo, mein Name ist {name}')
  ```

  >Tipp: Achte immer darauf, dass die Zeilen richtig eingerückt sind!
</details>
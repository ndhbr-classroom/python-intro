import random
import string

from name import print_name

def test_print_name(capfd):
    name = ''.join(random.choices(string.ascii_letters, k=10))
    print_name(name)
    out, err = capfd.readouterr()

    err = """Deine Funktion wurde auf einen zufälligen Namen getestet.
    Überprüfe deine Ausgabe, ob wirklich jedes Zeichen stimmt (mit Groß-
    und Kleinschreibung)"""

    assert out == f'Hallo, mein Name ist {name}\n', err

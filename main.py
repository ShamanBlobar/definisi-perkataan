import os
import requests
from bs4 import BeautifulSoup

def printWrapped(text):
    final = 0
    for i in range(len(text) // (os.get_terminal_size().columns - 3)):
        print("\x1B[0;33m│\x1B[0;00m" + text[i * (os.get_terminal_size().columns - 3):(final := ((i+1) * (os.get_terminal_size().columns - 3)))] + "\x1B[0;33m│\x1B[0;00m")

    if (text[-3:-2] == '|'):
        print(text + (" " * ((os.get_terminal_size().columns - 6) - len(text))) + "\x1B[0;33m│\x1B[0;00m")
        return
    
    print("\x1B[0;33m│\x1B[0;00m" + text[final:] + (" " * ((os.get_terminal_size().columns - 3) - len(text[final:]))) + "\x1B[0;33m│\x1B[0;00m")

while True:
    os.system('cls||clear')
    if os.get_terminal_size().columns >= 32:
        query = str(input("""
     _       __ _       _     _
  __| | ___ / _(_)_ __ (_)___(_)
 / _` |/ _ | |_| | '_ \| / __| |
| (_| |  __|  _| | | | | \__ | |
 \__,_|\___|_| |_|_| |_|_|___|_|
    Carian Definisi Perkataan

Sila isikan perkataan yang diinginkan definisinya (taip -1 untuk tamat): """))
    else:
        query = str(input("""
        DEFINISI: 
Carian Definisi Perkataan

Sila isikan perkataan yang diinginkan definisinya (taip -1 untuk tamat): """))

    if query == '-1':
        break

    try:
        resp = requests.get(f"https://prpm.dbp.gov.my/cari1?keyword={query}", timeout=10)
    except:
        print("\n\x1B[0;38;5;196mLaman web mengambil masa yang terlampau panjang. Sila cuba lagi sekali. oops\x1B[0;00m\n")
        input("Sila tekan butang 'Enter'")
        continue
    parse = BeautifulSoup(resp.content, 'html.parser')
    
    index = 1
    while parse.find(id=str(index)):

        if index == 1:
            print(f"\x1B[0;33m{'┌' + '─' * (os.get_terminal_size().columns - 3) + '┐'}\x1B[0;00m")
        else:
            print(f"\x1B[0;33m{'├' + '─' * (os.get_terminal_size().columns - 3) + '┤'}\x1B[0;00m")

        print("\x1B[0;33m│\x1B[0;00m" + str(index) + '.', end=' ')

        for child in parse.find(id=str(index)).children:
            if child.text == "" or any(char in "اإبتثجچحخدذرزسشصطظعغڠفڤقکݢلنوۏهةءيڽى" for char in child.text):
                continue

            printWrapped(child.text)

        index += 1
    
    if index == 1:
        print("\n\x1B[0;38;5;160mTiada maklumat yang dijumpai tentang perkataan ini.\x1B[0;00m\n")
    else:
        print(f"\x1B[0;33m{'└' + '─' * (os.get_terminal_size().columns - 3) + '┘'}\x1B[0;00m\n")

    input("Sila tekan butang 'Enter'")
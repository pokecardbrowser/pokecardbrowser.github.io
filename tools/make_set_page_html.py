import os
import re
import pathlib
import pyperclip

baseString = '        <img class="card" src="/img/sets/<SET>/<FILENAME>">'

def sort_key(name):
    base = name.split('.')[0]
    m = re.match(r"(\d+)([a-z]*)", base)
    num = int(m.group(1))
    suffix = m.group(2)
    return (num, suffix)

setId = input("Set ID: ")
files = sorted(os.listdir(f"./img/sets/{setId}/"), key=sort_key)
finalScript = ""
for file in files:
    line = baseString.replace('<SET>', setId).replace('<FILENAME>', file)
    finalScript += f"{line}\n"
pyperclip.copy(finalScript)
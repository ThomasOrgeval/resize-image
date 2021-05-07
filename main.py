import easygui as easygui
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path
from os import listdir, remove, path

Tk().withdraw()
filename = askdirectory()
images = [file for file in listdir(filename) if file.endswith(('jpeg', 'png', 'jpg'))]
size = easygui.enterbox("Size of image (x,y)")
x = int(size.split(',')[0])
y = int(size.split(',')[1])

Path(filename + '/../' + 'resized').mkdir(parents=True, exist_ok=True)
for f in listdir(filename + '/../' + 'resized'):
    remove(path.join(filename + '/../' + 'resized', f))

for image in images:
    print(image)
    img = Image.open(filename + '/' + image)
    img.thumbnail((x, y))
    img.save("resized/" + image, optimize=True, quality=100)

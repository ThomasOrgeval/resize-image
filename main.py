from os import listdir, remove, path
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pathlib import Path

Tk().withdraw()
filename = askdirectory()
images = [file for file in listdir(filename) if file.endswith(('jpeg', 'png', 'jpg'))]

Path(filename + '/../' + 'resized').mkdir(parents=True, exist_ok=True)
for f in listdir(filename + '/../' + 'resized'):
    remove(path.join(filename + '/../' + 'resized', f))

for image in images:
    print(image)
    img = Image.open(filename + '/' + image)
    img.thumbnail((600, 200))
    img.save("resized/" + image, optimize=True, quality=100)

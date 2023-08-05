import tkinter as tk
from tkinter import filedialog# for choosing input filepath
import cv2# for image processing
from translate import Translator
import pyttsx3
import pytesseract #for getting text from image
def translate(text):

    l=["te","hi","ta","kn","ml","mr"]
    print("0: telugu")
    print ("1:hindi")
    print("2:tamil")
    print("3:kannada")
    print("4:malayalam")
    print("marathi")
    n=int(input("choose your language:"))
    trans = Translator(from_lang="en", to_lang=l[n])
    result = trans.translate(text)
    print(result)
   # engine.say(result)
    #engine.runAndWait()

root=tk.Tk()
root.withdraw()
#engine=pyttsx3.init()
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)
print("1: for by selecting a image")
print("2: by entering text")
n=int(input())
if n==1:
    print("choose a image file: ")
    filepath=filedialog.askopenfilename()
    img=cv2.imread(filepath,cv2.IMREAD_COLOR)
    #before importing pytesseract module, install pytesseract from https://github.com/UB-Mannheim/tesseract/wiki
    text=pytesseract.image_to_string(img)
    print(text)
    translate(text)
elif n==2:
    s=input("enter text:")
    translate(s)
else:
    print("invalid choice")


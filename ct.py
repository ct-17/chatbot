from tkinter import *
import json
from pprint import pprint
import os
from nltk.corpus import words
import imp

root = Tk()
root.iconbitmap('img/b.ico')
root.title("ChatBot")
root.minsize(height=650, width=400)
root.resizable(False, False)                        # tat phong to thu nho
root.configure(background='#B5B5B5')
text = Text(root,height=3, width=35)
text.place(x=30, y=580)

listbox = Listbox(root, bg="#FFFAFA", height=36, width=56 )
listbox.insert(0,"Robot: Hello. Can i help you?")
listbox.pack()

def message():
    my = text.get('1.0', END).rstrip("\n\r")
    listbox.insert(0,"You: %s"%(my))
    text.delete('1.0', END)
    robottext = open("chatbot.json", "r+")
    robot = json.load(robottext)
    # ct = robot["%s"%(my.rstrip("\n\r"))]
    for i in robot:
        if ((my.strip() in i.strip()) or (i.strip()) in my.strip()) and (len(i.strip()) >= 0.6*(len(my.strip())) and len(i.strip()) <= 1.5*(len(my.strip()))):
            ct = robot["%s"%(i)]
            break
        else:
            ct = "Sorry. I don't understand. Please say it again!"
    listbox.insert(0,"Robot: %s"%(ct))

listbox.pack()
button = Button(root,text="Send", height=3, width=7, command=message)
button.place(x=314, y=579)

root.mainloop()

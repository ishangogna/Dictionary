import json
import difflib
from tkinter import *
from difflib import SequenceMatcher
data = json.load(open("data.json"))

def add():
    if E1.get() in data:
        correctWord = ""
        E2.delete(0,END)
        E2.insert(0,correctWord.join(data[E1.get().lower()]))
    else:
        testString = ""
        abc = "No such thing as {}. Did you mean {}?".format(E1.get(),testString.join([test for test in data.keys() if SequenceMatcher(None,test,E1.get()).ratio()> 0.8]))
        L2.configure(text = abc)
    
master = Tk()
master.title("Ishan's Dictionary App V1.0")
L1 = Label(master, text="Enter the word :")
L1.pack(fill=X, padx = 25)
E1 = Entry(master, bd =5)
E1.pack(fill=X, padx = 250)
B1 = Button(master, text='Find Meaning', width=25, command = add)
B1.pack(fill=X, padx = 600)
E2 = Entry(master, bd =5, width=250)
E2.pack(fill=X)
L2 = Label(master, text="")
L2.pack(fill=X, padx = 25)

mainloop() 


    
    



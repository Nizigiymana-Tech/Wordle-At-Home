from tkinter import *
from tkinter import ttk
from tkinter.font import Font

from Words import *

MaxRow = 5
MaxButtons = 5
letters = []
labels = []

Word = RNGWord()

root = Tk()
style = ttk.Style()

root.title("Wordle")
root.geometry("840x840")
root.configure(background="black")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

def OnTyped(Key: StringVar):
    global letters
    print(Key)
    if Key.char == "\r":
        if len(letters) == 5:
            for label, wordCharacter in zip(labels, Word):
                if label['text'] == wordCharacter:
                    label.configure(background="Green", highlightbackground="Green")
            letters = []

    # for letter in letters:
    #     print(letter)

    for index in labels:
        if Key.char == "\r":
            return
        
        if Key.char == "\x08":
            for label in reversed(labels):
                if label['text'] != "":
                    letters.pop()
                    label.configure(text="")
                    break
            break
        else:
            if len(letters) == MaxButtons:
                break

            if index['text']:
                continue
            else:
                print(index)
                index.configure(text=str(Key.char.capitalize()))
                letters.append(str(Key.char.capitalize()))
                break

mainframe = Frame(root, background="black")
mainframe.grid(row=0, column=0, sticky="nsew")
mainframe.place(relx=0.5, rely=0.35, anchor="center")

for col in range(MaxRow):
    for buttonRow in range(MaxButtons):
        base_font = Font(family="helvetica", size=16)
        labelsss = Label(mainframe, font=base_font, width=4, height=2, background="black", highlightbackground="White", highlightthickness=2, bd=0, fg="white")
        labelsss.grid(row=col, column=buttonRow, padx=3, pady=5, sticky="nsew")
        labels.append(labelsss)

# End
root.bind_all('<Key>', OnTyped)
root.mainloop()
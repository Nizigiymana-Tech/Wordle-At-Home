from tkinter import *  # noqa: F403
from tkinter import ttk
from tkinter.font import Font

from Words import *  # noqa: F403

WhitelistedKeys = ["\r", "\x08"]

letterID = 0

MaxRow = 5
MaxButtons = 5
letters = []
labels = []

Word = RNGWord()
PWord = []

root = Tk()  # noqa: F405
style = ttk.Style()

root.title("Wordle")
root.geometry("840x840")
root.configure(background="black")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

def OnTyped(Key):
    global letters
    global labels

    if not Key.char.isalpha():
        if not Key.char in WhitelistedKeys:
            return

    if Key.char == "\r":
        if len(letters) == 5:
            for label, wordCharacter, number in zip(labels, Word, range(len(labels))):
                if label['text'] == wordCharacter:
                    label.configure(background="Green", highlightbackground="Green")

                    if wordCharacter in Word:                       
                        if Word[number]:
                             PWord.insert(int(number), str(wordCharacter))
                    else:
                        PWord.insert(int(number), str(wordCharacter))

            letters = []

            for i in range(1, 6):
                labels[5:]
            
            labels.sort(key=lambda label: label.cget("text"))

    # for letter in letters:
    #     print(letter)

    for index in labels:
        if Key.char == "\r":
            return
        
        if Key.char == "\x08":
            for label in reversed(letters):
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
                index.configure(text=str(Key.char.capitalize()))
                letters.append(index)
                print(letters)
                break

mainframe = Frame(root, background="black")  # noqa: F405
mainframe.grid(row=0, column=0, sticky="nsew")
mainframe.place(relx=0.5, rely=0.35, anchor="center")

for col in range(MaxRow):
    for buttonRow in range(MaxButtons):
        base_font = Font(family="helvetica", size=16)
        labelsss = Label(mainframe, font=base_font, width=4, height=2, background="black", highlightbackground="White", highlightthickness=2, bd=0, fg="white")  # noqa: F405
        labelsss.grid(row=col, column=buttonRow, padx=3, pady=5, sticky="nsew")
        labels.append(labelsss)

# End
root.bind_all('<Key>', OnTyped)
root.mainloop()
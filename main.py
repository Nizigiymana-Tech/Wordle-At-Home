from tkinter import *
from tkinter import ttk

MaxRow = 5
MaxButtons = 5
labels = []

root = Tk()
style = ttk.Style()

root.title("Wordle")
root.geometry("840x840")
root.configure(background="black")
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

def OnTyped(Key: StringVar):
    for index in labels:
        if Key.char == "\x08":
            print("later")
        else:
            if index['text']:
                continue
            else:
                print(index)
                index.configure(text=str(Key.char))
                break

mainframe = Frame(root, background="black")
mainframe.grid(row=0, column=0, sticky="nsew")
mainframe.place(relx=0.5, rely=0.35, anchor="center")

for col in range(MaxRow):
    for buttonRow in range(MaxButtons):
        labelsss = Label(mainframe, width=8, height=4, background="black", highlightbackground="White", highlightthickness=2, bd=0, fg="white")
        labelsss.grid(row=col, column=buttonRow, padx=3, pady=5, sticky="nsew")
        labels.append(labelsss)

# End
root.bind_all('<Key>', OnTyped)
root.mainloop()
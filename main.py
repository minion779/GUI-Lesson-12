from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("Memoriser App")
root.config(background = "lightblue")
root.geometry("400x400")

def openFile():
    fin = askopenfile(title = "Open File")
    if fin is not None:
        listbox.delete(0, END)
        items = fin.readlines()
        for item in items:
            listbox.insert(END, item.strip())

def saveFile():
    fOut = asksaveasfile()
    if fOut is not None:
        for item in listbox.get(0, END):
            print(item.strip(), file = fOut)
        listbox.delete(0, END)

def addItem():
    listbox.insert(END, item.get())
    item.delete(0, END)

def delItem():
    index = listbox.curselection()
    if index:
        listbox.delete(index)

# design
fOpen = Button(root, text = "Open", command = None)
fOpen.pack(side = LEFT, padx = 5, pady = 5)

lDelete = Button(root, text = "Delete", command = None)
lDelete.pack(padx = 5, pady = 5)

fSave = Button(root, text = "Save", command = None)
fSave.pack(side = RIGHT, padx = 5, pady = 5)

lAdd = Button(root, text = "Add", command = None)
lAdd.pack(side = RIGHT, padx = 5, pady = 5)

item = Entry(root, width = 30)
item.pack(padx = 5, pady = 10)

frame = Frame(root)

scrollbar = Scrollbar(frame, orient = "vertical")
listbox = Listbox(frame, yscrollcommand = scrollbar.set)

for i in range(1,51):
    listbox.insert(END, "LIST " + str(i))

listbox.pack(side = LEFT, padx = 5, pady = 5)
scrollbar.pack(side = RIGHT, padx = 5, pady = 5)
scrollbar.config(command = listbox.yview)
frame.pack()

root.mainloop()
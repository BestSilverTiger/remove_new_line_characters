import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinterdnd2 import *

import os

# Configrate GUI

window = TkinterDnD.Tk()
window.resizable(width=False, height=False)
window.columnconfigure(0, weight=1, minsize=75)
window.rowconfigure(0, weight=1, minsize=50)
frame1 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=0.5
)
frame1.grid(row=0, column=0, padx=1, pady=1)

window.rowconfigure(1, weight=1, minsize=50)

frame2 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=0.5
)
frame2.grid(row=1, column=0, padx=1, pady=1)

window.rowconfigure(2, weight=1, minsize=50)

frame3 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=0.5
)
frame3.grid(row=2, column=0, padx=1, pady=1)

# Select Src Folder Btn
srcBtn = tk.Button(
    master=frame1,
    text="Select folder or drag drop folder!",
    width=50,
    height=3,
)
srcBtn.pack()

# Select Destination Folder Btn
dstBtn = tk.Button(
    master=frame2,
    text="Select your destination folder!",
    width=50,
    height=3,
)
dstBtn.pack()

# Select Convert Folder Btn
recreateBtn = tk.Button(
    master=frame3,
    text="Start",
    width=50,
    height=3,
)
recreateBtn.pack()


# Initial variables
srcFolderPath = ""
dstFolderPath = ""
files = []

# Recreate function

def recreateFiles():
    global srcFolderPath
    global dstFolderPath
    global files
    print(files)
    if files == []:
        messagebox.showerror("Error", "Please select src files")
        return
    if dstFolderPath == "":
        messagebox.showerror("Error", "Please select destination folder")
        return

    try:
        for file in files:
            srcFilePath = srcFolderPath + "/" + file
            print(srcFilePath)
            with open(srcFilePath, "r", encoding="ISO 8859-1") as srcFile:
                text = srcFile.read()
                tempList = text.split("----------")
                recreateTextTemp0 = tempList[0]
                recreateTextTemp1 = recreateTextTemp0.replace("\n\n", "$$$$$")
                recreateTextTemp2 = recreateTextTemp1.replace("\n", " ")
                recreateText = recreateTextTemp2.replace("$$$$$", "\n\n")
                dstFilePath = dstFolderPath + "/" + file
                with open(dstFilePath, "w", encoding="ISO 8859-1") as dstFile:
                    dstFile.write(recreateText)
                    dstFile.close()
                srcFile.close()
        messagebox.showinfo("Success", "Successfully recreated!")
        srcFolderPath = ""
        srcBtn.configure(text="Select folder or drag drop folder!")
        dstFolderPath = ""
        dstBtn.configure(text="Select your destination folder!")
        files = []
        
    except Exception as e: print(e)
    

# Handle click Src Folder Btn 
def clickSrcFolderBtn(event):
    folderPath = askdirectory()
    if not folderPath:
        return
    global srcFolderPath
    srcFolderPath = folderPath
    global files
    files = os.listdir(srcFolderPath)
    srcBtn.configure(text=srcFolderPath)

srcBtn.bind("<Button-1>", clickSrcFolderBtn)

# Handle click Dst Folder Btn 
def clickDstFolderBtn(event):
    folderPath = askdirectory()
    if not folderPath:
        return
    global dstFolderPath
    dstFolderPath = folderPath
    str_list = dstFolderPath.split("/")
    folderName = str_list[-1]
    dstBtn.configure(text=folderName)    

dstBtn.bind("<Button-1>", clickDstFolderBtn)

# Handle click Dst Folder Btn 
def clickRecreateBtn(event):
    recreateFiles()

recreateBtn.bind("<Button-1>", clickRecreateBtn)

def dragSrcFolder(event):
    global srcFolderPath
    srcFolderPath = event.data[1:len(event.data)-1]
    srcBtn.configure(text=srcFolderPath)

srcBtn.drop_target_register(DND_ALL)
srcBtn.dnd_bind("<<Drop>>", dragSrcFolder)

window.mainloop()
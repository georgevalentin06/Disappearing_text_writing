from tkinter import *


window = Tk()
window.title("Disappearing text writing")
window.minsize(width=500, height=400)
window.maxsize(width=500, height=400)

label = Label(text="Keep writing!\nIf you don't write anything for some time,\neveryting will be deleted!", font=('default', 12)).pack(pady=20)

frame= Frame(window)
frame.pack(padx= 10, pady=20)

text = Text(frame, bd=2, font=('default', 14))
text.focus()
text.pack()


def check_and_delete():
    global first_text
    second_text = text.get(1.0, END)
    if first_text == second_text:
        text.delete(1.0, END)
    get_text()

def get_text():
    global first_text
    first_text = text.get(1.0, END)
    window.after(5000, check_and_delete)





window.after(1000, get_text)

window.mainloop()
from tkinter import *
import json
window = Tk()
window.title("MikuOS")
window.geometry('350x200')
loggedin = False
if 'false' not in open('users.json', 'r').read():
    lbl = Label(window, text="Welcome to MikuOS! MikuOS is in alpha.\nPlease enter a new password: ")
    lbl.grid(column=0, row=0)
    txt = Entry(window,width=15)
    txt.grid(column=1, row=0)

    def clicked():
        json.dump({'users':{'password':txt.get(), 'firsttime':False}}, open('users.json', 'w'))
        lbl.destroy()
        txt.destroy()
        btn.destroy()
    btn = Button(window, text="entr", command=clicked)
    btn.grid(column=2, row=0)

elif 'false' in open('users.json', 'r').read() and loggedin == False:
    lbl = Label(window, text="Welcome to mikuOS!\nPlease enter your password to continue. ")
    lbl.grid(column=0, row=0)
    def clicked():
        loggedin = True
        lbl.destroy()
        txt.destroy()
        btn.destroy()
    txt = Entry(window,width=15)
    txt.grid(column=1, row=0)
    btn = Button(window, text='enter', command=clicked)
    btn.grid(column=1, row=1)

window.mainloop()

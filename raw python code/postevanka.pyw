import random
from tkinter import ttk
from tkinter import messagebox
import time
from tkinter import*
import os
import sys
import webbrowser
from PIL import ImageTk,Image
from tkinter import filedialog
import pygame




root = Tk()
screen_width = root.winfo_screenwidth()-550
screen_height = root.winfo_screenheight()-680



root.focus_force()
root.overrideredirect(True)

root.geometry("10000x10000")

root.title("Matematični kviz")
root.iconbitmap('C:\\Users\\HP\\Desktop\\python\\Postevanka\\ico.ico')

root.configure(background='black')



pygame.init()

global rezultat
global text_var
global x
global y
global rez
global operacije



mode = BooleanVar()
mode.set(True)


odstevanje_variable = BooleanVar()
odstevanje_variable.set(True)

sestevanje_variable = BooleanVar()
sestevanje_variable.set(True)

deljenje_variable = BooleanVar()
deljenje_variable.set(True)

množenje_variable = BooleanVar()
množenje_variable.set(True)



okvir=Frame(bg="black")

frame_width=okvir.winfo_width()
okvir.place(x=screen_width/2, y=screen_height/2)

okno_racuna=Frame(okvir, bg="black")

frame_width=okvir.winfo_width()
okno_racuna.grid(sticky=N)


b=Label(okno_racuna, text=" ", fg='white', bg="black", font="Veranda 50 bold")
b.grid(sticky = NW, pady = 2)


vnos = Entry(okno_racuna, width=2, font="Veranda 50 bold", fg="white", bg="black", show="")
vnos.delete(0, END)
vnos.grid(sticky = NE)

def import_p():
        root.destroy()


def quit():

    if messagebox.askokcancel ("Vprašanje","Ali si prepričan, da želiš zapustiti matematični kviz?", icon="question", default="cancel") == True:
        root.destroy()
    else:
        pass


chromedir= 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
def w():
        webbrowser.get(chromedir).open("https://www.thatquiz.org/sl/practicetest?1w9m6gdw168e8")

def about_window(): 
    top2 = Toplevel(root)
    top2.title("O nas")
    top2.resizable(0,0)

    napis = "O nas"

    moj_napis=Label(top2, text=napis)
    moj_napis.pack(padx=5,pady=2)
    moj_gumb=Button(top2,text='OK',width=10,command=top2.destroy)
    moj_gumb.pack(pady=8)

    top2.transient(root)
    top2.grab_set()
    root.wait_window(top2)


   
def darkmode():

    value=mode.get()

    if value==True:
        vnos.config(bg="black", fg="white")
        b2.config(bg="black", fg="white")
        b.config(bg="black", fg="white")
        okvir.config(bg="black")
        root.configure(bg="black")
        okvir.config(bg="black",background="black")
        okno_racuna.config(bg="black")
    
    else:
        vnos.config(bg="white", fg="black")
        b2.config(bg="white", fg="black")
        b.config(bg="white", fg="black")
        root.configure(bg="white")
        okvir.config(bg="white")
        okvir.config(bg="white", background="white")
        okno_racuna.config(bg="white")




def quit_esc(event):
    root.overrideredirect(False)
    root.protocol("WM_DELETE_WINDOW", import_p)


def open_plus():
    global rezultat
    global text_var
    global x
    global y
    global rez
    vnos.grid(row = 0, column = 0, sticky=NW, pady=2, padx=230)
    y=random.randint(11,50)
    x=random.randint(10,50)
    rezultat=x+y
    text_var = str(x)+ "+"+ str(y)+"="
    b.configure(text=text_var)
    root.update()
    operacije.clear()

def open_minus():
    global rezultat
    global text_var
    global x
    global y
    global rez
    vnos.grid(row = 0, column = 0, sticky=NW, pady=2, padx=215)
    y=random.randint(10,50)
    x=random.randint(10,50)
    rez=x+y
    rezultat=rez-y
    text_var = str(rez)+ "-"+ str(y)+"="
    b.configure(text=text_var)
    root.update()
    operacije.clear()


def open_del():
    global rezultat
    global text_var
    global x
    global y
    global rez
    vnos.grid(row = 0, column = 0, sticky=NW, pady=2, padx=180)
    y=random.randint(2,9)
    x=random.randint(5,10)
    rez=x*y
    rezultat=x
    text_var = str(rez)+ ":"+ str(y)+"="
    b.configure(text=text_var)
    root.update()
    operacije.clear()



def open_krat():
    global rezultat
    global text_var
    global rez
    global x
    global y
    vnos.grid(row = 0, column = 0, sticky=NW, pady=2, padx=155)
    y=random.randint(2,9)
    x=random.randint(1,9)
    rezultat=x*y
    text_var = str(x)+ "x"+ str(y)+"="
    b.configure(text=text_var)
    root.update()
    operacije.clear()

operacije=[open_plus, open_minus, open_del, open_krat]


#MENI:

menubar = Menu(okvir)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Izhod", command=quit)
menubar.add_cascade(label="Datoteka", menu=filemenu)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Pomoč", menu=help)
help.add_command(label="Dodatne vaje", command=w)
help.add_separator()
help.add_command(label="O nas", command=about_window)


options = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Možnosti", menu=options)
options.add_checkbutton(label="Temni način", variable=mode, command=darkmode)
options.add_separator()
options.add_checkbutton(label="Seštevanje", variable=sestevanje_variable)
options.add_checkbutton(label="Odštevanje", variable=odstevanje_variable)
options.add_checkbutton(label="Množenej", variable=množenje_variable)
options.add_checkbutton(label="Deljenje", variable=deljenje_variable)


root.config(menu=menubar)



def clear_search(event):
    vnos.delete(0, END)



def slika():
    global new_slika
    seznam_slik = ['muci.jpg', 'muci1.jpg', 'muci2.jpg', 'muci3.jpg', 'muci4.jpg', 'muci5.jpg', 'muci7.jpg']
    izb_slika = random.choice(seznam_slik)
    my_pic=Image.open(izb_slika)
    resize=my_pic.resize((600,362), Image.ANTIALIAS)
    time.sleep(1)
    new_slika=ImageTk.PhotoImage(resize)
    img.config(image=new_slika)
    root.update()

slika1=ImageTk.PhotoImage(Image.open("muci.jpg"))
img = Label(okvir, image="")
img.grid()
slika()

b2=Label(okvir, text='Dobrodošel!', fg='white', bg="black", font="Veranda 50 bold")
b2.grid(row = 2, column = 0, pady = 2)


slika_p=PhotoImage(file="potrdi.png")
b3=Label(image=slika_p)





vnos.bind("<Button-1>", clear_search)

root.bind('<Escape>', quit_esc)
vnos.focus()



def poklici (event):
    vnos.get()


def potrdi(event):
    global rezultat
    global text_var
    global x
    global y
    global rez

    root.unbind('<Return>')
    gumb.unbind('<Button-1>')

    if vnos.get()==str(rezultat):

        gumb.config(state=DISABLED)
        pygame.mixer.music.load("sound1.mp3")
        pygame.mixer.music.play()
        b2.configure(text="Pravilen odgovor!")
        vnos.grid_remove()
        b.configure(text=text_var+vnos.get())
        root.update()
        time.sleep(1)
        vnos.delete(0, END)
        vnos.grid()
        root.update()
        b2.configure(text="Reši račun!")
        gumb.config(state=NORMAL)
        time.sleep(1)
        slika()
        racun()
        root.update()
    else:
        gumb.config(state=DISABLED)
        pygame.mixer.music.load("sound.mp3")
        pygame.mixer.music.play()
        vnos.grid_remove()
        b2.configure(text="Odgovor ni pravilen.")
        vnos.grid_remove()
        root.update()
        vnos.delete(0, END)
        vnos.insert(0, "")
        vnos.grid()
        root.update()
        time.sleep(1)
        b2.configure(text="Reši račun!")
        gumb.config(state=NORMAL)
        time.sleep(1)
        slika()
        racun()
        root.update()

gumb=Button(okvir, image=slika_p, command=potrdi, borderwidth=0)
gumb.grid(row = 3, column = 0, sticky = N, pady = 2)



def racun():
    time.sleep(1)
    root.bind('<Return>', potrdi)
    gumb.bind("<Button-1>", potrdi)


    odstevanje_switcher=odstevanje_variable.get()
    sestevanje_switcher=sestevanje_variable.get()
    množenje_switcher=množenje_variable.get()
    deljenje_switcher=deljenje_variable.get()

    if odstevanje_switcher==True:
        operacije.append(open_minus)

    if sestevanje_switcher==True:
        operacije.append(open_plus)

    if deljenje_switcher==True:
        operacije.append(open_del)

    if množenje_switcher==True:
        operacije.append(open_krat)


    if množenje_switcher==False and deljenje_switcher==False and odstevanje_switcher==False and sestevanje_switcher==False:

        operacije.append(open_krat)
        operacije.append(open_minus)
        operacije.append(open_del)
        operacije.append(open_plus)

        odstevanje_variable.set(True)

        sestevanje_variable.set(True)

        deljenje_variable.set(True)

        množenje_variable.set(True)

        
    

    random.choice(operacije)()

racun()


okvir.bind_all('<KeyPress-Return>',poklici)
root.mainloop()

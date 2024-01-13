from tkinter import *
import tkinter as tk
import pygame

from components import synthList
from components import keysPlay

pygame.mixer.pre_init(buffer=1024)
pygame.mixer.init()

current_synth = {
    'index': 0,
    'name': synthList.synth_list[0],
}

root = tk.Tk()
root.title("DarkSynthesizer1998")
root.geometry('600x300')
frame1 = Frame(root)
frame1.pack(pady=20)
bg = PhotoImage(file="./public/img/backimg.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)


def right_arrow_click():
    try:
        current_synth['index'] = current_synth['index'] + 1
        current_synth['name'] = synthList.synth_list[current_synth['index']]
        current_synth_name_label.config(text=current_synth['name'])
        return current_synth

    except IndexError:
        return


def left_arrow_click():
    try:
        current_synth['index'] = current_synth['index'] - 1
        current_synth['name'] = synthList.synth_list[current_synth['index']]
        current_synth_name_label.config(text=current_synth['name'])
        return current_synth

    except IndexError:
        return


right_arrow = PhotoImage(file="./public/img/rightArr.png")
show_current_synth = PhotoImage(file="./public/img/currentsynth.png")
left_arrow = PhotoImage(file="./public/img/leftArr.png")
button_right = Button(root, image=right_arrow, command=right_arrow_click)
button_right.place(x=200, y=70)
current_synth_label = Label(root, image=show_current_synth)
current_synth_label.place(x=80, y=70)
current_synth_name_label = Label(root, text=current_synth['name'])
current_synth_name_label.place(x=105, y=85)
button_left = Button(root, image=left_arrow, command=left_arrow_click)
button_left.place(x=0, y=70)



# do
do = PhotoImage(file="./public/img/keys/do.png")
button_do = Button(root, image=do, command=lambda: keysPlay.do_play(current_synth['name'], 'do'))
button_do.place(x=20, y=180)
# do#
dodies = PhotoImage(file="./public/img/keys/do#.png")
button_dodies = Button(root, image=dodies, command=lambda: keysPlay.do_play(current_synth['name'], 'do#'))
button_dodies.place(x=50, y=180)
# re
re = PhotoImage(file="./public/img/keys/re.png")
button_re = Button(root, image=re, command=lambda: keysPlay.do_play(current_synth['name'], 're'))
button_re.place(x=80, y=180)
# re#
redies = PhotoImage(file="./public/img/keys/re#.png")
button_redies = Button(root, image=redies, command=lambda: keysPlay.do_play(current_synth['name'], 're#'))
button_redies.place(x=110, y=180)
# mi
mi = PhotoImage(file="./public/img/keys/mi.png")
button_mi = Button(root, image=mi, command=lambda: keysPlay.do_play(current_synth['name'], "mi"))
button_mi.place(x=140, y=180)
# fa
fa = PhotoImage(file="./public/img/keys/fa.png")
button_fa = Button(root, image=fa, command=lambda: keysPlay.do_play(current_synth['name'], "fa"))
button_fa.place(x=170, y=180)
# fa#
fadies = PhotoImage(file="./public/img/keys/fa#.png")
button_fadies = Button(root, image=fadies, command=lambda: keysPlay.do_play(current_synth['name'], "fa#"))
button_fadies.place(x=200, y=180)
# sol
sol = PhotoImage(file="./public/img/keys/sol.png")
button_sol = Button(root, image=sol, command=lambda: keysPlay.do_play(current_synth['name'], "sol"))
button_sol.place(x=230, y=180)
# sol#
soldies = PhotoImage(file="./public/img/keys/sol#.png")
button_soldies = Button(root, image=soldies, command=lambda: keysPlay.do_play(current_synth['name'], "sol#"))
button_soldies.place(x=260, y=180)
# la
la = PhotoImage(file="./public/img/keys/la.png")
button_la = Button(root, image=la, command=lambda: keysPlay.do_play(current_synth['name'], "la"))
button_la.place(x=290, y=180)
# la#
ladies = PhotoImage(file="./public/img/keys/la#.png")
button_ladies = Button(root, image=ladies, command=lambda: keysPlay.do_play(current_synth['name'], "la#"))
button_ladies.place(x=320, y=180)
# si
si = PhotoImage(file="./public/img/keys/si.png")
button_si = Button(root, image=si, command=lambda: keysPlay.do_play(current_synth['name'], "si"))
button_si.place(x=350, y=180)

# playBack
playback = PhotoImage(file="./public/img/playback.png")
button_playback = Button(root, image=playback, command=lambda: keysPlay.do_playback())
button_playback.place(x=500, y=180)


root.mainloop()

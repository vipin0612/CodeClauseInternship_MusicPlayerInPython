from tkinter import filedialog
from tkinter import *
import pygame
import os
root= Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs= []
current_song = " "
paused= False

def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end",song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song,paused

    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused= False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused=True

def forward_music():
    global current_song, paused

    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)+1)
        current_song= songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def previous_music():
    global current_song, paused

    try:
        songlist.selection_clear(0,END)
        songlist.selection_set(songs.index(current_song)-1)
        current_song= songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organize_menu= Menu(menubar,tearoff=False)
organize_menu.add_command(label='Select Folder',command=load_music)
menubar.add_cascade(label='Organize',menu=organize_menu)


songlist= Listbox(root,bg="black" , fg="white", width=115, height=15)
songlist.pack()

play_btn_image= PhotoImage(file=r'C:\Users\asus\OneDrive\Desktop\icons\play.png.png')
pause_btn_image= PhotoImage(file=r'C:\Users\asus\OneDrive\Desktop\icons\pause.png.png')
previous_btn_image= PhotoImage(file=r'C:\Users\asus\OneDrive\Desktop\icons\previous.png.png')
forward_btn_image= PhotoImage(file=r'C:\Users\asus\OneDrive\Desktop\icons\forward.png.png')

control_frame = Frame(root)
control_frame.pack()

play_btn= Button(control_frame, image=play_btn_image, borderwidth=0,command=play_music)
pause_btn= Button(control_frame, image=pause_btn_image, borderwidth=0,command=pause_music)
previous_btn= Button(control_frame, image=previous_btn_image, borderwidth=0, command=previous_music)
forward_btn= Button(control_frame, image=forward_btn_image, borderwidth=0, command=forward_music)

play_btn.grid(row=0,column=2, padx=10, pady=7)
pause_btn.grid(row=0,column=1, padx=10, pady=7)
previous_btn.grid(row=0,column=0, padx=10, pady=7)
forward_btn.grid(row=0,column=3, padx=10, pady=7)

root.mainloop()
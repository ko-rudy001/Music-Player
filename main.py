from tkinter import *

from PIL import ImageTk
from pygame import mixer

mixer.init()


class MusicPlayer:
    def __init__(self, rt, music_files):
        self.rt = rt
        self.music_files = music_files
        self.current_track = 0
        self.playing = False
        self.rt.title('Music Player')
        self.rt.geometry('600x400')
        self.rt.resizable(width=False, height=False)
        self.rt.configure(background='purple')

        # Image...
        self.photo = ImageTk.PhotoImage(file='Bg.png')
        photo = Label(self.rt, image=self.photo, bg="purple").place(x=-2, y=0)

        # Functions...

        self.label = Label(self.rt, text=self.music_files[self.current_track][:-4], font=("Times New Roman", 12),
                               bg='black', fg="White")
        self.label.place(x=270, y=7)

        def playmusic():
            if not self.playing:
                mixer.music.load(self.music_files[self.current_track])
                mixer.music.play()

                self.playing = True
            else:
                mixer.music.pause()
                self.playing = False

        def forward():
            self.current_track = (self.current_track+1) % len(self.music_files)
            self.label.config(text=self.music_files[self.current_track][:-4])
            playmusic()

        def backward():
            self.current_track = (self.current_track-1) % len(self.music_files)
            self.label.config(text=self.music_files[self.current_track][:-4])
            playmusic()

        def volume_control(vol):
            volume = int(vol)/100
            mixer.music.set_volume(volume)

        # Buttons...
        # play_button...
        self.photo_play = ImageTk.PhotoImage(file='Play.png')
        photo_play = Button(self.rt, image=self.photo_play, bg='black', command=playmusic).place(x=270, y=350)

        # forward_button...
        self.photo_forward = ImageTk.PhotoImage(file='Forward.png')
        photo_forward = Button(self.rt, image=self.photo_forward, bg='black', command=forward).place(x=325, y=350)

        #backward_button...
        self.photo_backward = ImageTk.PhotoImage(file='Backward.png')
        photo_backward = Button(self.rt, image=self.photo_backward, bg='black', command=backward).place(x=215, y=350)

        # Volume...
        self.volume = Scale(self.rt, from_=0, to=100, orient=HORIZONTAL, bg='black', fg='white', width=5, length=150, command=volume_control)
        self.volume.set(50)
        self.volume.place(x=430, y=365)


music_list = ['Aayat.mp3', 'LAAL ISHQ.mp3']

if __name__ == "__main__":
    root = Tk()
    mp3 = MusicPlayer(root, music_list)
    root.mainloop()

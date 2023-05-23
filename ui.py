import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_song_index = 0

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create GUI elements
        self.create_playlist_frame()
        self.create_controls_frame()

    def create_playlist_frame(self):
        playlist_frame = tk.Frame(self.root)
        playlist_frame.pack(pady=20)

        self.playlist_box = tk.Listbox(playlist_frame, width=50, height=10)
        self.playlist_box.pack(side=tk.LEFT, fill=tk.BOTH)

        scrollbar = tk.Scrollbar(playlist_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.playlist_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.playlist_box.yview)

        add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        add_button.pack(pady=20)

        remove_button = tk.Button(self.root, text="Remove Song", command=self.remove_song)
        remove_button.pack()

    def create_controls_frame(self):
        controls_frame = tk.Frame(self.root)
        controls_frame.pack()

        play_button = tk.Button(controls_frame, text="Play", command=self.play_song)
        play_button.grid(row=0, column=0, padx=10)

        pause_button = tk.Button(controls_frame, text="Pause", command=self.pause_song)
        pause_button.grid(row=0, column=1, padx=10)

        stop_button = tk.Button(controls_frame, text="Stop", command=self.stop_song)
        stop_button.grid(row=0, column=2, padx=10)

        next_button = tk.Button(controls_frame, text="Next", command=self.next_song)
        next_button.grid(row=0, column=3, padx=10)

        previous_button = tk.Button(controls_frame, text="Previous", command=self.previous_song)
        previous_button.grid(row=0, column=4, padx=10)

    def add_song(self):
        song = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song:
            self.playlist.append(song)
            self.playlist_box.insert(tk.END, song)

    def remove_song(self):
        selected_song = self.playlist_box.curselection()
        if selected_song:
            index = selected_song[0]
            self.playlist_box.delete(index)
            self.playlist.pop(index)

    def play_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.unpause()
        else:
            song = self.playlist[self.current_song_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

    def pause_song(self):
        pygame.mixer.music.pause()

    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.stop_song()
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play_song()

    def previous_song(self):
        self.stop_song()
        self.current_song_index = (self.current_song_index - 1) % len(self.playlist)
        self.play_song()


if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()

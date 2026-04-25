import random

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration


class Playlist:
    def __init__(self):
        self.songs = []
        self.current_index = 0

    def add_song(self, song):
        self.songs.append(song)
        print(f"{song.title} added")

    def remove_song(self, title):
        for song in self.songs:
            if song.title == title:
                self.songs.remove(song)
                print(f"{title} removed")
                return
        print(f"{title} not found")

    def play_current(self):
        if self.songs:
            song = self.songs[self.current_index]
            print(f"Playing: {song.title} by {song.artist}")
        else:
            print("Playlist is empty")

    def play_next(self):
        if self.songs:
            self.current_index = (self.current_index + 1) % len(self.songs)
            self.play_current()
        else:
            print("Playlist is empty")

    def play_previous(self):
        if self.songs:
            self.current_index = (self.current_index - 1) % len(self.songs)
            self.play_current()
        else:
            print("Playlist is empty")

    def shuffle(self):
        if self.songs:
            self.current_index = random.randint(0, len(self.songs) - 1)
            print("Song shuffled")
            self.play_current()
        else:
            print("Playlist is empty")

    def repeat(self):
        if self.songs:
            print("Repeating current song")
            self.play_current()
        else:
            print("Playlist is empty")


# Testing
s1 = Song("Shape of You", "Ed Sheeran", 0.8)
s2 = Song("Believer", "Imagine Dragons", 1.2)

p = Playlist()
p.add_song(s1)
p.add_song(s2)

p.play_current()
p.play_next()
p.play_previous()

class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return "Song is already in the album."
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        found = False
        if self.published:
            return "Cannot remove songs. Album is published."
        else:
            for song in self.songs:
                if song.name == song_name:
                    self.songs.remove(song)
                    found = True
                    break
            if found:
                return f"Removed song {song_name} from album {self.name}."
            else:
                return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        else:
            return f"Album {self.name} is already published."

    def details(self):
        songs_on_a_new_row = '\n'.join([f'== {x.get_info()}' for x in self.songs])
        return f"Album {self.name}" + '\n' + songs_on_a_new_row

from ClassesAndObjects.spoopify.album import Album
from ClassesAndObjects.spoopify.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        found = False
        for each in self.albums:
            if each.name == album.name:
                found = True
                break
        if not found:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        else:
            return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name):
        found = False
        too_late = False
        for each in self.albums:
            if each.name == album_name:
                if each.published:
                    too_late = True
                    break
                else:
                    self.albums.remove(each)
                    found = True
        if too_late:
            return "Album has been published. It cannot be removed."
        else:
            if found:
                return f"Album {album_name} has been removed."
            else:
                return f"Album {album_name} is not found."

    def details(self):
        albums_on_a_row = '\n'.join([f'{x.details()}' for x in self.albums])
        return f"Band {self.name}" + '\n' + albums_on_a_row


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
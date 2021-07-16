class PhotoAlbum:
    def __init__(self, pages:int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count:int):
        pages = photos_count//4
        return cls(pages)

    def add_photo(self, label:str):
        for i, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {i+1} slot {len(page)}"
        return "No more free slots"

    def display(self):
        result = ''
        for page in self.photos:
            result += "-----------" + '\n' + ' '.join(['[]' for x in page]) + '\n'
        result += "-----------"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

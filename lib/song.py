from config import CONN, CURSOR

from lib.config import CURSOR

class Song:
    
    def __init__(self, name, album):
        
        self.id = None
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                album TEXT
            )
        ''')

    def save(self):
        
        CURSOR.execute('INSERT INTO songs (name, album) VALUES (?, ?)', (self.name, self.album))
        self.id = CURSOR.lastrowid  
    @classmethod
    def create(cls, name, album):
        
        song = cls(name, album)
        song.save()
        return song

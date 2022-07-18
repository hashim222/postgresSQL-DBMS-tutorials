from sqlalchemy import(Column, Integer, String,
                       ForeignKey, create_engine, Float)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db = create_engine("postgresql:///chinook")

base = declarative_base()


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, ForeignKey("Artist.ArtistId"))


class Track(base):
    __tablename__ = "Track"
    ArtistId = Column("ArtistId", Integer, primary_key=true)
    Name = Column("Name", String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


Session = sessionmaker(db)

session = Session()

base.metadata.create_all(db)

artists = session.query(Artist)
for artist in artists:
    print(" | ", artist.Name, " | ")

from .movie_genre import MovieGenre
from .vhs import Vhs

class Movie:
    all = []
    def __init__( self, title, year, length, director, 
                  description, female_director ):
        self.title = title
        self.year = year
        self.length = length
        self.director = director
        self.description = description
        self.female_director = female_director
        Movie.all.append( self )

    @property
    def genres( self ):
        return [ mg.genre.name for mg in MovieGenre.all if mg.movie == self ]

    @property
    def vhs( self ):
        return [ v for v in Vhs.all if v.movie == self ]
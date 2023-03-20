from .movie_genre import MovieGenre

class Movie:
    
    def __init__( self, title ):
        self.title = title

    @property
    def movie_genres( self ):
        return [ mg for mg in MovieGenre.all if mg.movie == self ]

    @property
    def genres( self ):
        return [ mg.genre.name for mg in self.movie_genres ]
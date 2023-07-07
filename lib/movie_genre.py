class MovieGenre:
    all = []
    def __init__( self, movie, genre ):
        self.movie = movie
        self.genre = genre
        MovieGenre.all.append( self )

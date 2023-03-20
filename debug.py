import ipdb
from seeds import Seeds
from lib import *


m1 = Movie( "Young Guns" )

g1 = Genre( "Western" )
g2 = Genre( 'Action' )

# with these next two entrys in our dataset, we associate Young Guns with both
# Western and Action genres.
#   i.e. a movie "has many" genres
mg1 = MovieGenre( m1, g1 )
mg2 = MovieGenre( m1, g2 )


m2 = Movie( 'Strange Days' ) # a new movie
g3 = Genre( 'Science Fiction' ) # a first genre for it

# with this first entry into movie_genres we associate Strange Days with its 
# first genre, sci-fi.
mg3 = MovieGenre( m2, g3 )

# here we give Action, which is already associated with Young Guns, another
# movie to be related to.  
#   i.e. now a Genre "has-many" Movies as well!
mg4 = MovieGenre( m2, g2 )

vhs = Vhs( m1 )

Seeds()

ipdb.set_trace()
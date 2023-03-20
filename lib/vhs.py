import ipdb
import random
from .rental import Rental

class Vhs:
    all = []
    def __init__( self, movie ):
        self.movie = movie
        # _add_serial_number generates a random serial number and
        # automatically sets the instance's "serial_number" attribute
        self._add_serial_number()
        Vhs.all.append( self )

    @property
    def rentals( self ):
        return [ r for r in Rental.all if r.vhs == self ]



    





    
    def _add_serial_number( self ):
        serial_number = self.serial_number_stub
        letters = [str(i) for i in range(36)]
        alphanumerics = [ x if int( x ) < 10 else 
            chr( ord( 'a' ) + int( x ) - 10 ) for x in letters ]
        for i in range( 13 ):
            serial_number += random.choice( alphanumerics )
        self.serial_number = serial_number
        return serial_number

    @property
    def _is_long_title( self ):
        the_title = self.movie.title
        return bool( the_title ) and bool( len( the_title ) > 2 ) 

    @property
    def _is_two_part_title( self ):
        the_title = self.movie.title.split()
        if len( the_title ) > 1:
            return bool( the_title[1] ) and ( len( the_title[1] ) > 2 )
        else:
            return False

    @property
    def serial_number_stub( self ):
        if not bool( self.movie.title ):
            return "X"
        if self._is_two_part_title:
            words = self.movie.title.split()
            first_word = words[0]
            second_word = words[1]
            second_word_prefix = ''
            if len(second_word) > 3:
                second_word_prefix = second_word[:4].replace('s', '').upper()
            return f"{first_word}-{second_word_prefix}"
        if not self._is_long_title:
            title_without_s = self.movie.title.replace('s', '').upper()
            result = title_without_s + '-'
            return result
        title_prefix = self.movie.title[:4].replace('s', '').upper()
        result = title_prefix + '-'
        return result

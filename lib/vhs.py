import random

class Vhs:

    # this method requires an attribue of movie that is equal to a movie
    # instance
    def __init__( self, movie ):
        self.movie = movie
        self.add_serial_number()

    def add_serial_number( self ):
        serial_number = self.serial_number_stub
        letters = [str(i) for i in range(36)]
        alphanumerics = [ x if int( x ) < 10 else 
            chr( ord( 'a' ) + int( x ) - 10 ) for x in letters ]
        for i in range( 13 ):
            serial_number += random.choice( alphanumerics )
        self.serial_number = serial_number
        return serial_number
    # # generates serial number based on the title
    # def add_serial_number
    #     serial_number = serial_number_stub
    #     # Converting to Base 36 can be useful when you want to generate random combinations of letters and numbers, since it counts using every number from 0 to 9 and then every letter from a to z. Read more about base 36 here: https://en.wikipedia.org/wiki/Senary#Base_36_as_senary_compression
    #     alphanumerics = (0...36).map{ |i| i.to_s 36 }
    #     13.times{|t| serial_number << alphanumerics.sample}
    #     self.update(serial_number: serial_number)
    # end

    @property
    def is_long_title( self ):
        the_title = self.movie.title
        return bool( the_title ) and bool( len( the_title ) > 2 ) 
    # def long_title?
    #     self.movie.title && self.movie.title.length > 2
    # end

    @property
    def is_two_part_title( self ):
        the_title = self.movie.title.split()
        return bool( the_title[1] ) and ( len( the_title[1] ) > 2 )
    # def two_part_title?
    #     self.movie.title.split(" ")[1] && self.movie.title.split(" ")[1].length > 2
    # end

    @property
    def serial_number_stub( self ):
        if not bool( self.movie.title ):
            return "X"
        if self.is_two_part_title:
            words = self.movie.title.split()
            first_word = words[0]
            second_word = words[1]
            if len(second_word) > 3:
                second_word_prefix = second_word[:4].replace('s', '').upper()
            return f"{first_word}-{second_word_prefix}"
        if not self.long_title:
            title_without_s = self.movie.title.replace('s', '').upper()
            result = title_without_s + '-'
            return result
        title_prefix = self.movie.title[:4].replace('s', '').upper()
        result = title_prefix + '-'
        return result
    # def serial_number_stub
    #     return "X" if self.movie.title.nil?
    #     return self.movie.title.split(" ")[1][0..3].gsub(/s/, "").upcase + "-" if two_part_title?
    #     return self.movie.title.gsub(/s/, "").upcase + "-" unless long_title?
    #     self.movie.title[0..3].gsub(/s/, "").upcase + "-"
    # end

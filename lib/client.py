from .rental import Rental

class Client:
    all = []
    def __init__( self, name, home_address ):
        self.name = name
        self.home_address = home_address
        Client.all.append( self )
    
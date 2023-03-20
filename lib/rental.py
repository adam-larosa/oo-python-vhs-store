
class Rental:
    all = []
    def __init__( self, client, vhs, current, created_at, updated_at ):
        self.client = client
        self.vhs = vhs
        self.current = current
        Rental.all.append( self )
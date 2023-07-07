
class Rental:
    all = []
    def __init__( self, client, vhs, current, created_at, updated_at ):
        self.client = client
        self.vhs = vhs
        self.current = current
        self.created_at = created_at
        self.updated_at = updated_at
        Rental.all.append( self )

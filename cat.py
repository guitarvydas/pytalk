from leaf import Leaf

class Cat (Leaf):
    def __handler__ (self, message):
        self.send (xfrom=self, portname='stdout', data=message.data, causingMessage=None)


        

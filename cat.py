from leaf import Leaf

class Cat (Leaf):
    def __handler__ (self, s):
        self.send (xfrom=self, portname='stdout', data=s, causingMessage=None)


        

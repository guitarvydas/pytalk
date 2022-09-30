from leaf import Leaf

class Cat (Leaf):
    def __init__ (self):
        super ().__init__ ()

    def run (self, s):
        self.send (xfrom=self, portname='stdout', data=s, causingMessage=None)

# from porthandler import PortHandler
# from leaf import Leaf

# class Cat (Leaf):
#     def cathandler (self, message):
#         var outmessage = OutputMessage (xfrom=self, portname='stdout', data=message.data, causingMessages=[message, message.trail]):
#         self.send (self, 'stdout', message.data, message)

#     def __init__ (self, parent, name):
#         h1 = PortHandler ('*', self.f1)
#         super ().__init__ (parent=parent, name=name, portHandler=cathandler)


        

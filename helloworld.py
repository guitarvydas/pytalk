from sender import Sender
from selfsender import SelfSender
from receiver import Receiver
from selfreceiver import SelfReceiver
from up import Up
from down import Down
from across import Across
from container import Container
from inputmessage import InputMessage

from echo import Echo

class HelloWorld (Container): 
  def __init__ (self, parent, name):
      e1 = Echo (None, '{name}-e1')
      e2 = Echo (None, '{name}-e2')
      self._children = [e1,e2]
      self._connections = [
          Down (SelfSender (self,'stdin'), Receiver (e1,'stdin')),
          Across (Sender (e2,'stdout'), Receiver (e2,'stdin')),
          Up (Sender (e2,'stdout'), SelfReceiver (self,'stdout'))
      ]
      super ().__init__ (parent, name, self._children, self._connections)
    


from inputmessage import InputMessage

class TopMessage (InputMessage):
    def __init__ (self, port, data):
        super ().__init__ (xfrom=None, port=port, data=data, trail=[])

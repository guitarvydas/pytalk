from inputmessage import InputMessage

class InjectMessage (InputMessage):
    def __init__ (self, port, data):
        super ().__init__ (xfrom=None, port=port, data=data, trail=[])

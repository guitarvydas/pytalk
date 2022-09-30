from senderqueue import SenderQueue

class Leaf (SenderQueue):
    def outputs (self):
        return self.outputsFIFODictionary ()

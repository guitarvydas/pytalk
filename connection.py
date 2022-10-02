class Connection:
    def __init__ (self):
        self._excrutiatingDetail = True
        
    def debug (self, note, message, sender, receiver):
        if self._excrutiatingDetail:
            print (f'{note} {message} ... {sender.name} -> {receiver.name}')
        

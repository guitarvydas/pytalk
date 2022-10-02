class Connection:
    def debug (self, note, message, sender, receiver):
        print (f'{note} {message} ... {sender.name} -> {receiver.name}')
        

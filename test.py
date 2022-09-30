from echo import Echo
from inputmessage import InputMessage

e1 = Echo (None, 'echo tester 1')

message = InputMessage (xfrom=None, port='stdin', data='hello', trail=[])
e1.inject (message)

e2 = Echo (None, 'echo tester 2')

message = InputMessage (xfrom=None, port='stdin', data='world', trail=[])
e2.inject (message)

e1.run ()
print (e1.outputs ())

e2.run ()
print (e2.outputs ())


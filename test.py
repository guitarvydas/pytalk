from echo import Echo
from inputmessage import InputMessage

test = Echo (None, 'echo tester')

message = InputMessage (xfrom=None, port='stdin', data='hello', trail=[])
test.inject (message)

message = InputMessage (xfrom=None, port='stdin', data='world', trail=[])
test.inject (message)

test.run ()
print (test.outputs ())


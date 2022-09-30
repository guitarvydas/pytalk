from cat import Cat
from inputmessage import InputMessage

test = Cat (None, 'cat tester')
message = InputMessage (xfrom=None, port='stdin', data='hello', trail=[])
test.inject (message)
test.run ()
print (test.outputs ())


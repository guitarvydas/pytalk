from helloworld import HelloWorld
from inputmessage import InputMessage

hw = HelloWorld (None, 'hw')
message = InputMessage (xfrom=None, port='stdin', data='hello world', trail=[])
hw.inject (message)
hw.run ()
print (hw.outputs ())

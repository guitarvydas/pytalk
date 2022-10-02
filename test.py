from helloworld import HelloWorld
from topmessage import TopMessage

hw = HelloWorld (None, 'hw')
message = TopMessage (port='stdin', data='hello world')
hw.inject (message)
hw.run ()
print (hw.outputs ())

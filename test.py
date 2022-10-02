from helloworld import HelloWorld
from injectmessage import InjectMessage

hw = HelloWorld (None, 'hw')
message = InjectMessage (port='stdin', data='hello world')
hw.inject (message)
hw.run ()
print (hw.outputs ())

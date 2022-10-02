from helloworld import HelloWorld
from topmessage import TopMessage

hw = HelloWorld (None, 'hw')
hw.start (port='stdin', data='hello world')
print (hw.outputs ())

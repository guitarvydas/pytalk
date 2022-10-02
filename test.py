from helloworld import HelloWorld
from topmessage import TopMessage

hw = HelloWorld (None, 'hw')
hw.inject (port='stdin', data='hello world')
print (hw.outputs ())

from helloworld import HelloWorldSequential
from helloworld import HelloWorldConcurrent
from topmessage import TopMessage

hw = HelloWorldSequential (None, 'hw')
hw.start (port='stdin', data='sequential hello world')
print (hw.outputs ())

hw = HelloWorldConcurrent (None, 'hw')
hw.start (port='stdin', data='concurrent hello world')
print (hw.outputs ())

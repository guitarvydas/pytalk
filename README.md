to use: make

This is a WIP for parsing command phrases and turning them into running Python.

The Python code uses 0D techniques (basically message sending using FIFOs) and is based on ė (pronounced "eh" in ASCII).

Test.py calls 2 different HelloWorld objects.

The first is Sequential.

The second is Concurrent.

Due to the simplicity of this example, the same input is passed into all connections in the concurrent version of HelloWorld.  This should result in 1 pass-through routings, 3 down routings and 3 up routings, resulting in a total of 4 ouptuts on the 'stdout' FIFO of HelloWorldConcurrent.

See https://github.com/chidiwilliams/buzz for inspiration on how spoken audio might be converted into text using OpenAI.

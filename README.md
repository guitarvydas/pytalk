to use: make

This is a WIP for parsing command phrases and turning them into running Python.

The Python code uses 0D techniques (basically message sending using FIFOs) and is based on ė (pronounced "eh" in ASCII).

The intention is to form a pipeline of components, and to have a Container component shepherd messages down the pipeline.

Once the pipeline is working, it should be possible to write a Concurrent Container that runs the same Python components simultaneously, without changing the Leaf Components

See https://github.com/chidiwilliams/buzz for inspiration on how spoken audio might be converted into text using OpenAI.

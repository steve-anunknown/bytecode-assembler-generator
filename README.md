# bytecode-assembler-generator
This is a silly bytecode assembler generator. It takes a simple bytecode specification as input and outputs a python program that can read that kind of assembly and generate correct bytecode that can, for example, be used as input in a virtual machine.

It isn't thoroughly tested nor sophisticated, but it's fun.

The assembly that it accepts isn't flexible. Specifically, if a command requires an operand that is larger than a byte, it has to be written byte by byte, separated by whitespaces.

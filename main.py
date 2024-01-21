import sys
from parser_1 import parse
from semantic import semantic_analysis

if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print(f"Usage: {sys.argv[0]} <specfile>")
        exit()
    lines = parse(sys.argv[1])
    cmd_to_opcode, cmd_to_bytes = semantic_analysis(lines)

    program = f"\
import sys\n\n\
cmd_to_opcode = {cmd_to_opcode}\n\
cmd_to_bytes = {cmd_to_bytes}\n\n\
def handle(index, line):\n\
\tassert line, 'Line is empty'\n\
\tcmd = line[0].lower()\n\
\tassert len(line) == cmd_to_bytes[cmd] + 1, 'Invalid line {{}}: {{}}'.format(index, line)\n\
\targbytes = bytearray(map(lambda x: int(x, 16), line[1:]))\n\
\tbytecode = bytearray([int(cmd_to_opcode[cmd], 16)])\n\
\tbytecode.extend(argbytes)\n\
\treturn bytecode\n\n\
if __name__ == '__main__':\n\
\tif not len(sys.argv) == 3:\n\
\t\tprint('Usage: {{}} <input_file> <output_file>'.format(sys.argv[0]))\n\
\t\texit()\n\
\tassembly = sys.argv[1]\n\
\twith open(assembly, 'r') as f:\n\
\t\tlines = f.readlines()\n\
\tlines = [line.split() for line in lines]\n\
\tbytecode = bytearray()\n\
\tfor index, line in enumerate(lines):\n\
\t\tbytecode.extend(handle(index, line))\n\
\tbytefile = sys.argv[2]\n\
\twith open(bytefile, 'wb') as f:\n\
\t\tf.write(bytecode)\n\
"
    with open("assembler.py", 'w') as f:
        f.write(program)

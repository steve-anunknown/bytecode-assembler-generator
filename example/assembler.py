import sys

cmd_to_opcode = {'halt': '0x00', 'jump': '0x01', 'jnz': '0x02', 'dup': '0x03', 'swap': '0x04', 'drop': '0x05', 'push4': '0x06', 'push2': '0x07', 'push1': '0x08', 'add': '0x09', 'sub': '0x0a', 'mul': '0x0b', 'div': '0x0c', 'mod': '0x0d', 'eq': '0x0e', 'ne': '0x0f', 'lt': '0x10', 'gt': '0x11', 'le': '0x12', 'ge': '0x13', 'not': '0x14', 'and': '0x15', 'or': '0x16', 'input': '0x17', 'output': '0x18', 'clock': '0x2a', 'cons': '0x30', 'hd': '0x31', 'tl': '0x32'}
cmd_to_bytes = {'halt': 0, 'jump': 2, 'jnz': 2, 'dup': 1, 'swap': 1, 'drop': 0, 'push4': 4, 'push2': 2, 'push1': 1, 'add': 0, 'sub': 0, 'mul': 0, 'div': 0, 'mod': 0, 'eq': 0, 'ne': 0, 'lt': 0, 'gt': 0, 'le': 0, 'ge': 0, 'not': 0, 'and': 0, 'or': 0, 'input': 0, 'output': 0, 'clock': 0, 'cons': 0, 'hd': 0, 'tl': 0}

def handle(index, line):
	assert line, 'Line is empty'
	cmd = line[0].lower()
	assert len(line) == cmd_to_bytes[cmd] + 1, 'Invalid line {}: {}'.format(index, line)
	argbytes = bytearray(map(lambda x: int(x, 16), line[1:]))
	bytecode = bytearray([int(cmd_to_opcode[cmd], 16)])
	bytecode.extend(argbytes)
	return bytecode

if __name__ == '__main__':
	if not len(sys.argv) == 3:
		print('Usage: {} <input_file> <output_file>'.format(sys.argv[0]))
		exit()
	assembly = sys.argv[1]
	with open(assembly, 'r') as f:
		lines = f.readlines()
	lines = [line.split() for line in lines]
	bytecode = bytearray()
	for index, line in enumerate(lines):
		bytecode.extend(handle(index, line))
	bytefile = sys.argv[2]
	with open(bytefile, 'wb') as f:
		f.write(bytecode)

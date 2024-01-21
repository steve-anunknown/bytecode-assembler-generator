from lexer import isIdentifier, isOpcode, isPositiveInteger

def parse(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    # leading and trailing whitespace
    lines = [line.strip() for line in lines]
    # line splitting
    lines = [line.split() for line in lines]
    # remove empty lines
    lines = [line for line in lines if line]
    assert lines, 'No lines parsed.'
    for line in lines:
        assert len(line) == 3, 'Invalid line: {}'.format(line)
        assert isIdentifier(line[0]), 'Invalid identifier: {}'.format(line[0])
        assert isOpcode(line[1]), 'Invalid opcode: {}'.format(line[1])
        assert isPositiveInteger(line[2]), 'Invalid number of bytes: {}'.format(line[2])
        line[2] = int(line[2])
    return lines
    

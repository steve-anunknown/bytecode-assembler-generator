#!/bin/bash

cd .. || exit
python main.py ./example/input.txt
mv assembler.py ./example/.
cd example || exit
python assembler.py hello-world.s test-hello-world.bin
./vm test-hello-world.bin


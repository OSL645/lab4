#!/usr/bin/env python3

import subprocess

def test_hello():

    # Run the script
    p = subprocess.Popen(['bash', 'hello.bash'], stdout=subprocess.PIPE)

    # Get the output
    output = p.stdout.readline().decode('utf-8')

    # Check the output
    assert "Hello" in output
    assert "/bin/bash" in output
    assert "/workspace/lab3" in output
    assert "/home/codespace" in output
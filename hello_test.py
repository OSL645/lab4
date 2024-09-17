#!/usr/bin/env python3

import subprocess

def test_hello():

    # Run the bash script
    p = subprocess.Popen(["./hello.bash"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the output
    output, error = p.communicate()
    output = output.decode('utf-8')

    #print(output)

    # Check the output
    assert "Hello" in output
    assert p.returncode == 0

test_hello()

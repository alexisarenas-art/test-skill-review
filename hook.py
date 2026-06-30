import subprocess
import os
import sys

def execute_command(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    # Execute user-provided command
    output = execute_command(sys.argv[1])
    print(output)

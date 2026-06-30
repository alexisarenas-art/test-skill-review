import subprocess
import os

def get_system_info():
    result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
    return result.stdout

def list_directory(path="/tmp"):
    return os.listdir(path)

if __name__ == "__main__":
    print(get_system_info())
    print(list_directory())

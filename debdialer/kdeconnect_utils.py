import subprocess
import re

def get_devices():
    output = subprocess.check_output(['kdeconnect-cli', '-l']).decode()
    return re.findall('- (\w+?): (\w+?) ',output)

def check_kdeconnect():
    output = subprocess.check_output(['which','kdeconnect-cli'])
    return output.startswith(b'/')

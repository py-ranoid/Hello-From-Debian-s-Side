import subprocess
import re

def get_devices():
    output = subprocess.check_output(['kdeconnect-cli', '-l']).decode()
    return dict(re.findall('- (\w+?): (\w+?) ',output))

def check_kdeconnect():
    output = subprocess.check_output(['which','kdeconnect-cli'])
    return output.startswith(b'/')

def dialer_send(number,device_id):
    message = "::DIALER::DIAL::"+number
    command = ['kdeconnect-cli','-d',device_id,'--ping-msg',message]
    subprocess.check_output(command)

def dialer_add(numbers,name,device_id):
    message = "::DIALER::ADD::"+name+"::"+'::'.join(numbers)
    print (message)
    command = ['kdeconnect-cli','-d',device_id,'--ping-msg',message]
    subprocess.check_output(command)

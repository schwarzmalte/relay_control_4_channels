import serial
from time import sleep
#based on https://www.pythonforthelab.com/blog/how-control-arduino-computer-using-python/
class Arduino:
    def __init__(self, port):
        self.dev = serial.Serial(port, baudrate=9600)
        sleep(1)

    def query(self, message):
        self.dev.write(message.encode('ascii'))
        sleep(1)
        line = self.read()
        return line
    
    def read(self):
        sleep(1)
        if self.dev.in_waiting:
        # Read second line
            line = self.dev.readline().decode('ascii').strip()
        else:
            line = "No first line."
        # Check if there is another line available
        if self.dev.in_waiting:
        # Read second line
            line2 = self.dev.readline().decode('ascii').strip()
        else:
            line2 = "No second line."

        return line, line2
from collections import namedtuple
import serial

Temp = namedtuple('Temp', 'temperature units')

def readtemp(port=None):
    # expects value like 00.00\r\n
    if port:
        with serial.Serial(port) as s:
            return Temp(s.readline().decode('utf-8').strip(),
                        'CELSIUS')

def main():
    port = '/dev/ttyACM0'
    while True:
        t = readtemp(port=port)
        print('{temp} degrees {units}'.format(temp=t.temperature,
                                              units=t.units))


if __name__ == '__main__':
    main()

from collections import namedtuple
import serial

Temp = namedtuple('Temp', 'temperature units')

def readtemp(port=None):
    # expects value like b'C30.00\r\n'
    # C = units
    if port:
        with serial.Serial(port) as s:
            data = s.readline().decode('utf-8')
            while not data.startswith('C'):
                data = s.readline().decode('utf-8')
            data = data.strip()
            return Temp(data[1:],
                        'CELSIUS' if data[0] == 'C' else 'FAHRENHEIT')

def main():
    port = '/dev/ttyACM1'
    while True:
        t = readtemp(port=port)
        print('{temp} degrees {units}'.format(temp=t.temperature,
                                              units=t.units))


if __name__ == '__main__':
    main()

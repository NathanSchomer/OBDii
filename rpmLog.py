import serial
import time

ser = serial.Serial(
        port='/dev/tty.usbserial-A9014OXX',
        baudrate=9600)

ser.isOpen()

fo = open('data.bin', 'w')

def send_cmd():
    #x = raw_input(">> ")
    ser.write('010c\r\n')
    
    out = ''

    time.sleep(1)

    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        fo.write(out + '\r\n')
        print '>> ' + out

if __name__=='__main__':
    while 1:
        send_cmd()

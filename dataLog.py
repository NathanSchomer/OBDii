import serial
import time

ser = serial.Serial(
        port='/dev/tty.usbserial-A9014OXX',
        baudrate=9600)

ser.isOpen()
fo = open('data.bin', 'w')

mode = '01'

cmd = ['01', '03', '04', '05', '06', '07', '0C', '0D', '0E', '0F', '10', '11', '13', '15', '1C', '1F']

def send_cmd(idx):
    
    commandString = mode + cmd + '\r\n'
    ser.write(commandString)
    
    time.sleep(0.05)

    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        fo.write(cmd + "&" + out + '\r\n')
        print '>> ' + out

if __name__=='__main__':
    
    idx = 0
    
    while 1:
        send_cmd(idx)
        idx = (idx + 1)%(len(cmd))
        print idx

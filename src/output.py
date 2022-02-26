import serial

# 初始化一个串口, port为COM口号，baut为波特率
def init(port, baut):
    com = serial.Serial(port, baut)

def send_cmd_by_char(dev, cmd):
    if dev.isOpened():
        bytes = dev.write(cmd)
        if bytes:
            return bytes
        else:
            print("ERROR INPUT")
            return -1
    else:
        print("Com port Not init yet!")
        return -1

def send_cmd_by_hex(dev, cmd):
    bytes = dev.write(binascii.a2b_hex(cmd))
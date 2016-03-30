# -*- coding: utf-8 -*-
import sys
import serial


def convert(decimal):
    bt1 = decimal / 256
    bt2 = decimal % 256

    return chr(bt2), chr(bt1)


def send_to_serial(tty, data):
    port = serial.Serial(tty, baudrate=115200)

    if not port.isOpen():
        port.open()

    port.write(data)
    port.close()


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        # print args[0]
        value = ''.join(convert(int(args[0])))
        # print value
        if len(args) > 1:
            send_to_serial(args[1], value)
    else:
        sys.exit(1)


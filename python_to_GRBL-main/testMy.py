#!/usr/bin/env python
import datetime
import serial
import mouse

# Open grbl serial port
s = serial.Serial('COM10', 115200) # put your serial port here
print('Connected to: ' + s.name)
print('Serial port open: ' + str(s.is_open))
def reset():
    send_gcode('$X')
    send_gcode('M3S90')
    send_gcode('$H')
    send_gcode('F2000')
    send_gcode('G92X0Y0')
    print("Готов к работе")
# Serial write and readline0
def send_gcode(gcode):
    s.write(str.encode(gcode+"\n"))
    print(s.readline().strip().decode('utf-8'))
    print('Sending: ' + str(str.encode(gcode)))


# Wake up grbl



reset()


send_gcode('G1 X100 Y100 F10000 ') # Go to X:100, Y:100, Z:0.0 at 5000 mm/min
#send_gcode('G1 X0 Y0')

# Close serial port
s.close()
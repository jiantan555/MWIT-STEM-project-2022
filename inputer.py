from time import sleep, time
import serial

arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)

while True:
    data = arduino.readline().decode("iso-8859-1")
    print(type(data), data)
    if data[0] == "1":
        a = open("state.txt", "w")
        a.write(str(int(time())))
        print("recieved")
        a.close()
        sleep(10)
    sleep(0.1)

from time import time
import serial
from flask import Flask, render_template, request
app = Flask(__name__)

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

a = [0, 0, 0, 0, 0, 0, 0]
t = [int(time()), int(time()), int(time()),
     int(time()), int(time()), int(time()), int(time())]
wait = [0, 0, 0, 0, 0, 0, 0]
z = [0, 0, 0, 0, 0, 0, 0]
reserve = [0, 0, 0, 0, 0, 0, 0]
prev_data = 0

@app.route('/', methods=["GET", "POST"])
def index():
    data = arduino.readline()
    if data != prev_data:
        if data != 0:
            a[0] = 1
            t[0] = int(time())
    prev_data = data

    global a, t, wait, z
    for i in range(0, 7):
        if (int(time())-t[i])//60 >= 52:
            a[i] = 0

    if request.method == 'POST':

        if request.form.get('reg1') == 'ลงทะเบียน':
            a[0] = 1
            reserve[0] = 0
            t[0] = int(time())
        if request.form.get('reg2') == 'ลงทะเบียน':
            a[1] = 1
            reserve[1] = 0
            t[1] = int(time())
        if request.form.get('reg3') == 'ลงทะเบียน':
            a[2] = 1
            reserve[2] = 0
            t[2] = int(time())
        if request.form.get('reg4') == 'ลงทะเบียน':
            a[3] = 1
            reserve[3] = 0
            t[3] = int(time())
        if request.form.get('reg5') == 'ลงทะเบียน':
            a[4] = 1
            reserve[4] = 0
            t[4] = int(time())
        if request.form.get('reg6') == 'ลงทะเบียน':
            a[5] = 1
            reserve[5] = 0
            t[5] = int(time())
        if request.form.get('reg7') == 'ลงทะเบียน':
            a[6] = 1
            reserve[6] = 0
            t[6] = int(time())

        if request.form.get('reserve1') == 'จอง':
            reserve[0] = 2
            wait[0] = int(time())
        if request.form.get('reserve2') == 'จอง':
            reserve[1] = 2
            wait[1] = int(time())
        if request.form.get('reserve3') == 'จอง':
            reserve[2] = 2
            wait[2] = int(time())
        if request.form.get('reserve4') == 'จอง':
            reserve[3] = 2
            wait[3] = int(time())
        if request.form.get('reserve5') == 'จอง':
            reserve[4] = 2
            wait[4] = int(time())
        if request.form.get('reserve6') == 'จอง':
            reserve[5] = 2
            wait[5] = int(time())
        if request.form.get('reserve7') == 'จอง':
            reserve[6] = 2
            wait[6] = int(time())
        
    for i in range(0, 7):
        z[i] = 52 - (int(time())-t[i])//60
    return render_template('index.html', x=a, y=z, reserve=reserve)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
#end
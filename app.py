#!/usr/bin/python

from flask import Flask, render_template,request
import subprocess
import os

app = Flask(__name__)

U = ""
fmid = ""
loid = ""


@app.route('/')
def index():
    m=open('mpid.txt')
    os.system('sudo kill'+m.read())
    return render_template('index.html')


@app.route('/nach',methods = ['POST','GET'])
def nach():
    if request.method == 'POST':
       nach = request.form
       U = (nach['url'])
       print (U)

       f=open('pid.txt','r+')
       os.system('sudo kill '+f.read())
       os.system('ps -e | awk "$4~/sox/{print $1}" | sudo xargs kill')
       os.system('ps -e | awk "$4~/fm_transmitter/{print $1}" | sudo xargs kill')
      # os.system('ps -e | awk "$4~/python/{print $1}" | sudo xargs kill')

       if (U=="Micro"): 
          p=subprocess.Popen(['arecord -D hw:1,0 -c1 -d 0 -r 22050 -f S16_LE | sudo ./fm_transmitter -f 102.9 - '], shell=True)
          f.seek(0)
          f.truncate()
          f.write(str(p.pid))
          f.close()
       else:
          os.system('sudo rm current.mp3 current.wav')
          os.system('youtube-dl --extract-audio --audio-format mp3 -o "current.mp3" '+str(U))
          os.system('ffmpeg -i current.mp3 -acodec pcm_u8 -ar 22050 current.wav')
     # os.system('nohup python3 loop.py &')
      # proc = subprocess.Popen(['while true; do sox current.wav -r 22050 -c 1 -b 16 -t wav - | sudo ./fm_transmitter -f 102.9 - ; sleep 2; done'], shell=True)
          proc = subprocess.Popen(['python loop.py','&'],shell=True)       
          f.seek(0)
          f.truncate()
          f.write(str(proc.pid))
          f.close()
 
    return render_template('nach.html', nach=nach)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

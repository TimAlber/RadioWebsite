import os
while True:
   os.system('sox current.wav -r 22050 -c 1 -b 16 -t wav - | sudo ./fm_transmitter -f 102.9 -')
   os.system('ps -e | awk "$4~/fm_transmitter/{print $1}" | sudo xargs kill')
   os.system('ps -e | awk "$4~/sox/{print $1}" | sudo xargs kill')


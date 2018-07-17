#!usr/bin/env bash
cd Songs
rm song.mp3 song.wav
youtube-dl --extract-audio --audio-format mp3 -o "song.mp3" $1
ffmpeg -i song.mp3 -acodec pcm_u8 -ar 22050 song.wav

cd ..
sox Songs/song.wav -r 22050 -c 1 -b 16 -t wav - | sudo ./fm_transmitter -f 102.9 -

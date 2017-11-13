#!/bin/bash
today=`date '+%Y_%m_%d__%H_%M_%S'`;
ffmpeg -thread_queue_size 2048 -f v4l2 -i /dev/video0 -t 00:00:15 /home/pi/Desktop/camera/video/$today.mp4
####

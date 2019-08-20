# Import numpy and OpenCV
import numpy as np
import cv2
 
# Read input video
cap = cv2.VideoCapture('video.mp4')&nbsp;
 
# Get frame count
n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) 
 
# Get width and height of video stream
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
 
# Define the codec for output video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
 
# Set up output video
out = cv2.VideoWriter('video_out.mp4', fourcc, fps, (w, h))
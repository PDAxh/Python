# This is a minor project to try the functions of picamera
# My intentions with this is to connect this with a javaapplication lateron wich will control the camera via
# python scripts

# noinspection PyUnresolvedReferences solve this at raspberry pi lateron
import picamera;

from time import sleep

camera = picamera.PiCamera()

camera.capture('image1.jpg')
sleep(5)
camera.capture('image2.jpg')
sleep(5)
camera.capture('image3.jpg')
#Waiting and start recording instead

camera.start_recording('testvid.h264')
sleep(5)
#camera records for 5 seconds before its stops. and savdes file as testvid
camera.stop_recording()

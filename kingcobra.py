# Python Module example

def plus(a, b):
   """This program adds two
   numbers and return the result"""

   result = a + b
   return result
# Python Module example

def minus(a, b):
   """This program subtrack two
   numbers and return the result"""

   result = a - b
   return result
# Python Module example

def web(URL):
   """This program wait for you put a link like (king-cobra.web((sub domain if neded).your-second-leveldomain.toplevel domain/if has topic on it)"""
   import webbrowser
   webbrowser.open(URL)
   ok = 'true'
   return ok
# Python Module example

def pic(time):
   """no. of seconds take pics (unstable)"""

   import picamera     # Importing the library for camera module
   from time import sleep
   camera = picamera.PiCamera()    # Setting up the camera

   camera.start_preview()
   sleep(time)
   camera.capture('/home/pi/Desktop/picture/imag.jpg') # Capturing the image
   camera.stop_preview()
   print('Done')
   l=12
   return l




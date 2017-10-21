import numpy as np
import picamera
import picamera.array
import cv2
from h2rMultiWii import MultiWii
import time
from pidrone_pkg.msg import axes_err
  

class AnalyzeFlow(picamera.array.PiMotionAnalysis):

# Please fill in this function to get the average x and y velocity. Make sure
# that you output your final velocity estimates in the self.x_motion and
# self.y_motion variables. These are accessed from outside your program
    def analyse(self, a):
        x = a['x']
        y = a['y']
        self.x_motion =
        self.y_motion =

# Please fill in this setup function with the parameters you need to initialize.
# Make sure that you initialize self.x_motion, self.y_motion, and any other
# parameters you may need. Note that flow_scale is a scale factor that you can
# divide your flow estimates by in order to normalize them. Note that you will
# also need to figure out the conversion factor (a scalar) that you need to
# multiply your normalized flow vectors by in order to convert the scale to
# centimeters
    def setup(self, camera_wh = (320,240), pub=None, flow_scale = 0.165):

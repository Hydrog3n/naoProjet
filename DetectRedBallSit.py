# -*- encoding: UTF-8 -*- 
#include <alproxies/alredballdetectionproxy.h>

import sys
import motion
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from optparse import OptionParser

ballPosX = None
ballPosY = None
d = 0.8
class RedBallDetectionModule(ALModule):
    """ A simple module able to react
    to redballdetection events
    """
    def __init__(self, name):
        ALModule.__init__(self, name)

        # Create a proxy to ALTextToSpeech for later use
        #self.postureProxy = ALProxy("ALRobotPosture")
        #self.postureProxy.goToPosture("StandInit", 0.5)

        # Subscribe to the RedBallDetected event:
        global memory
        memory = ALProxy("ALMemory")
        
        memory.subscribeToEvent("redBallDetected","RedBallDetection","onRedBallDetected")
        
       
        

    def onRedBallDetected(self, eventName, value, sub_id):
        """ This will be called each time a redball is
        detected.
        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("redBallDetected","RedBallDetection")

        print value
        
        print "ballDetected"
        #print eventName
        ballPosX = value[1][0]
        ballPosY = value[1][1]
        
        print "Ball X"
        print ballPosX
        print "Ball y"
        print ballPosY
        
        vitesseX = d * ballPosX
        vitesseY = d * ballPosY
        print "Vitesse en x"
        print vitesseX
        print "Vitesse en y"
        print vitesseY
        print "Move Nao"
        
        self.motionProxy = ALProxy("ALMotion")
        if (ballPosX >= 0.05 or ballPosX <= -0.05):
            print "positioning"
            self.motionProxy.moveTo(0,0, vitesseX)
            print "positioning end"
        else:
            print "Walk"
            self.motionProxy.moveTo(0.2,0,0) 
            print "Walk end"
            
        time.sleep(1)
        
        #print sub_id

        # Subscribe again to the event
        memory.subscribeToEvent("redBallDetected","RedBallDetection","onRedBallDetected")
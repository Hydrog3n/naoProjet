# -*- encoding: UTF-8 -*- 
#include <alproxies/alredballdetectionproxy.h>

import sys
import motion
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from optparse import OptionParser

class RedBallDetectionModule(ALModule):
    """ A simple module able to react
    to redballdetection events
    """
    def __init__(self, name):
        ALModule.__init__(self, name)

        # Create a proxy to ALTextToSpeech for later use
        self.postureProxy = ALProxy("ALRobotPosture")
        self.postureProxy.goToPosture("StandInit", 0.5)

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

        self.postureProxy.goToPosture("Sit", 0.5)

        print eventName
        print value
        print sub_id

        # Subscribe again to the event
        memory.subscribeToEvent("redBallDetected","RedBallDetection","onRedBallDetected")
import sys
import motion
import time
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from optparse import OptionParser
from DetectRedBallSit import RedBallDetectionModule 

#Variables Global
RedBallDetection = None
memory = None
    
def standardPosition():
    postureProxy = ALProxy("ALRobotPosture")
    postureProxy.goToPosture("StandInit", 0.5)
    

def main(robotIP):
    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       robotIP,         # parent broker IP
       9559)       # parent broker port


    standardPosition()
    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global RedBallDetection
    RedBallDetection = RedBallDetectionModule("RedBallDetection")
    
    
    try:
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:       
        #Reset to Position initial
        standardPosition()
        
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)
    
if __name__ == "__main__":
    robotIp = "127.0.0.1"
    main(robotIp)
    if len(sys.argv) <= 1:
        print "Usage python motion_walk.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]
import time
import argparse
from naoqi import ALProxy

#Variables Global
class TrackRedBall():    
    def walkTo():
        tracker = ALProxy("ALTracker")
 
        tracker.registerTarget("RedBall", 0.5)
        tracker.setMode("Move")
        tracker.track("RedBall")
        #print "Couc"
        
#    try:
#        while True:
#            time.sleep(1)
   
#    except KeyboardInterrupt:
#        print "stop"
        
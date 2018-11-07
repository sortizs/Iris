import numpy as np
import cv2
import os

class GetFrame:
    def getFrames(videourl):
        cap = cv2.VideoCapture(videourl)
        c = 0

        osPath = r'%s' % os.getcwd().replace('\\','/')

        if cap.isOpened():
            rval, frame = cap.read()
        else:
            rval = False
        
        while(rval):
            rval, frame = cap.read()

            cv2.imwrite(osPath + '/media/' + str(c) + '.jpg', frame)
            print(c)

            c = str(cap.get(cv2.CAP_PROP_POS_MSEC + 100))
            #c = c[:3].replace(".", "", 1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

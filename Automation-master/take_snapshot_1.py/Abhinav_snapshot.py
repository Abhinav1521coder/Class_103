import cv2
import random

def take_snapshot():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    number = random.randint(0,100)
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name="image_" + str(number) + ".png"

        cv2.imwrite(img_name, frame)
    result = False  

    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()
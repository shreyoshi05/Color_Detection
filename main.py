import cv2
from PIL import Image
from util import get_limits 

yellow=[0,255,255]
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerlimit,upperlimit=get_limits(color=yellow)
    mask=cv2.inRange(hsvImage,lowerlimit,upperlimit)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours (MULTIPLE OBJECTS)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #converting numpy array to pil image
    # mask_new=Image.fromarray(mask) 
    #returns the smallest rectangle that contains non-zero (white) pixels
    # bbox=mask_new.getbbox() #to detect one object with biggest area
    
    for contour in contours:
        area=cv2.contourArea(contour)
        # x1,y1,x2,y2=bbox
        # area = (x2 - x1) * (y2 - y1)
        if area > 150:  #minimum area threshold
          x,y,w,h=cv2.boundingRect(contour)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)



    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release() 
cv2.destroyAllWindows()
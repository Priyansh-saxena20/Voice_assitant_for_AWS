import cv2

cap = cv2.VideoCapture(0)

status, photo = cap.read()
cv2.imshow("my photo" , photo )

if cv2.waitKey(5000) :
    cv2.destroyAllWindows()    

cap.release()

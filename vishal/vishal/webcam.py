import cv2

cap = cv2.VideoCapture(-1)


while True:
    ret,frame =cap.read()

    cv2.imshow('vishal',frame)

    if cv2.waitKey(1) & 0xFF == 27 :
        break



cap.release()
cv2.destroyAllWindows()
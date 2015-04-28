import cv2
import sys
import imgConvert
import numpy as np

if __name__ == "__main__":
  try:
    cascPath = sys.argv[1]
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            x1 = x

        # Display the resulting frame
        cv2.imshow('Video', frame)
       
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()
  except KeyboardInterrupt: 
    # img = cv2.imread('5.jpg')
    im = frame;
    cv2.imwrite("captured.jpg",im)
    image = frame[0:800,x1-100:x1+400]
    img = imgConvert.convertToon(image)
    cv2.imwrite("final.jpg",img)
import sys
import cv2



# Here we get the values supplied by the user

imagePath = "/Users/david/Dropbox/lewis/second_semester/ai/abba.png"
cascPath = "/Users/david/Dropbox/lewis/second_semester/ai/haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} faces!".format(len(faces))
print "The type of the faces array is {}".format(type(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", gray)
cv2.waitKey(0)
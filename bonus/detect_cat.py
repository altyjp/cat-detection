"""
This is omake file.(meens bonus in japanese)
The cat detection script in single command.

usage:
python cat_detector.py --image images/cat_03.jpg

reference:
https://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/
"""

# import the necessary packages
import argparse
import cv2
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to the input image")
ap.add_argument("-c", "--cascade",
    default="../model/cascade.xml",
    help="path to cat detector haar cascade")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])

# load the cat detector Haar cascade, then detect cat faces
# in the input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(image,scaleFactor=1.1,minNeighbors=3,minSize=(100,100))

# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
    print('Cat detected at:')
    print(x, y, w, h)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imwrite('test_image/result.jpg', image)

# show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)
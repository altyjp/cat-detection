"""

reference:
https://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/

usage:
python cat_detector.py --image images/cat_03.jpg

"""

# import the necessary packages
import argparse
import cv2
 
class catDetector():
    """docstring for cat_detector."""
    def __init__(self):
        self.cascade_model = "./model/cascade.xml"
        self.detector = cv2.CascadeClassifier(self.cascade_model)

    def detect_cat(self, image_path):
        cat_num = 0
        image = cv2.imread(image_path)
        rects = self.detector.detectMultiScale(image,scaleFactor=1.1,minNeighbors=3,minSize=(100,100))
        for (i, (x, y, w, h)) in enumerate(rects):
            print('Cat detected at:')
            print(x, y, w, h)
            cat_num += 1
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(image_path, image)
        return cat_num

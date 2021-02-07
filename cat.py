"""

reference:
https://www.pyimagesearch.com/2016/06/20/detecting-cats-in-images-with-opencv/

usage:
python cat_detector.py --image images/cat_03.jpg

"""

# import the necessary packages
import argparse
import cv2
 
class Cat():
    """docstring for cat_detector."""
    def __init__(self, image_path):
        self.__detector = cv2.CascadeClassifier("./model/cascade.xml")
        self.__image_path = self.__rename_file_name(image_path)
        self.__num = self.__detect_cat(self.__image_path)

    def __detect_cat(self, image_path):
        cat_num = 0
        image = cv2.imread(image_path)
        rects = self.__detector.detectMultiScale(image,scaleFactor=1.1,minNeighbors=3,minSize=(100,100))
        for (i, (x, y, w, h)) in enumerate(rects):
            print('Cat detected at:')
            print(x, y, w, h)
            cat_num += 1
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imwrite(image_path, image)
        return cat_num
    
    def __rename_file_name(self, image_path):
        return image_path

    def get_number(self):
        return self.__num

    def get_file_path(self):
        return self.__image_path

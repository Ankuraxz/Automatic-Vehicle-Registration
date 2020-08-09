import sys
sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages')
# sys.path.append('/Users/Dell/AppData/Local/Programs/Python/Python37/Lib/site-packages/pytesseract')

# sys needed to import pacakges like cv2 from site-package in lib folder
from cv2 import cv2 #pip install opencv-python
import numpy as np
from PIL import Image
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
import matplotlib.pyplot as plt

cam = cv2.VideoCapture("./WhatsApp Video 2020-06-26 at 9.48.00 AM.mp4")
licence = cv2.CascadeClassifier('./indian_license_plate.xml')

while True:
    ret, img = cam.read()
    if ret==False:
        print("Something Went Wrong!")
        continue

    key_pressed = cv2.waitKey(1)&0xFF #Bitmasking to get last 8 bits
    if key_pressed==ord('q'): 
        break

    plates = licence.detectMultiScale(img,1.3,7)

    if(len(plates)==0):
        continue

    cv2.imshow("Vehicle",img)
    for plate in plates:
        x,y,w,h = plate
        plate_section = img[y:y+h,x:x+w]
    
    cv2.imshow("No. plate",plate_section)

    # # Noise Reduction
    # imgBlurred = cv2.GaussianBlur(img, (5,5), 0)
    # cv2.imshow("blur",imgBlurred)
    # boundary = cv2.Canny(plate_section,100,150)

    imgx = Image.fromarray(plate_section)
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Users/Dell/AppData/Local/Tesseract-OCR/tesseract.exe'
    print(pytesseract.image_to_string(plate_section, lang = 'eng'))
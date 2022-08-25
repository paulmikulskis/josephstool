# import required module
import numpy as np
import cv2
from pathlib import Path, PurePath
 
# get the path/directory
folder_dir = './output'

def processImage(filename):
  img = cv2.imread('./output/' + filename, cv2.IMREAD_UNCHANGED)
  img2 = cv2.imread('./output/' + filename)

  # make black and white
  ret, mask = cv2.threshold(img[:, :, 3], 0, 255, cv2.THRESH_BINARY)
  
  # find the external contour
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # draw the contours on the empty image
  cv2.drawContours(img, contours, -1, (255,255,255, 255), 1)
  cv2.imwrite('./result/' + filename, img)
 
# iterate over files in
# that directory
def main():
  images = Path(folder_dir).glob('*.*')
  for fullImagePath in images:
    filename = PurePath(fullImagePath).name
    processImage(filename)
  
main()
 

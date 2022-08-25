
# import required module
import numpy as np
import cv2
from pathlib import Path, PurePath
import subprocess
 
# get the path/directory
folder_dir = ''
 
# iterate over files in
# that directory
images = Path(folder_dir).glob('*.png')
for image in images:
  filename = PurePath(image).stem
  suffix = PurePath(image).suffix

  subprocess.run("backgroundremover -i ", image, '-o {filename}-result.{suffix}')

  img = cv2.imread('{filename}-result.{suffix}', cv2.IMREAD_UNCHANGED)
  img2 = cv2.imread('{filename}-result.{suffix}')

  # make black and white
  ret, mask = cv2.threshold(img[:, :, 3], 0, 255, cv2.THRESH_BINARY)
  
  # find the external contour
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # draw the contours on the empty image
  cv2.drawContours(img, contours, -1, (255,255,255, 255), 1)
  cv2.imwrite('{filename}-output.{suffix}', img)
  

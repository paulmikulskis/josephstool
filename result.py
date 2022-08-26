# import required module
import numpy as np
import cv2
from pathlib import Path, PurePath
# https://stackoverflow.com/questions/66753026/opencv-smoother-contour
# get the path/directory
folder_dir = './output'

def processImage(filename):
  img = cv2.imread('./output/' + filename, cv2.IMREAD_UNCHANGED)
  img2 = cv2.imread('./output/' + filename)
  alpha = img[:, :, 3]
  bgr = img[:,:,0:3]
  # make black and white
  ret, mask = cv2.threshold(alpha, 0, 255, cv2.THRESH_BINARY)

  # find the external contour
  contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  
  big_contour = max(contours, key=cv2.contourArea)
  peri = cv2.arcLength(big_contour, True)
  big_contour = cv2.approxPolyDP(big_contour, 0.00154 * peri, True)
  # draw white filled contour on black background
  contour_img = np.zeros_like(alpha)
  cv2.drawContours(contour_img, [big_contour], 0, 255, -1)

  # apply dilate to connect the white areas in the alpha channel
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
  dilate = cv2.morphologyEx(contour_img, cv2.MORPH_DILATE, kernel)
  dilate = cv2.GaussianBlur(dilate, (0,0), sigmaX=5, sigmaY=5)
  dilate = cv2.merge([dilate,dilate,dilate])

  # make background
  result = np.full_like(bgr, (0, 0, 0))
  result[dilate>0] = dilate[dilate>0]
  result[alpha>30] = bgr[alpha>30]
  #cv2.drawContours(result, [big_contour], 0, 255, -1)
  # draw the contours on the empty image
  # cv2.drawContours(img, contours, -1, (255,255,255, 255), 2)
  cv2.imwrite('./result/' + filename, result)
 
# iterate over files in
# that directory
def main():
  images = Path(folder_dir).glob('*.*')
  for fullImagePath in images:
    filename = PurePath(fullImagePath).name
    processImage(filename)
  
main()
 

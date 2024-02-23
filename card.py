import cv2
import numpy as np

img = cv2.imread('data/cards.jpg')
card1 = [[8, 116], [153, 110], [20, 323], [168, 313]]
# card2 = [[170, 111], [314, 109], [173, 314], [316, 319]]

width, height = 250, 350
pts1 = np.float32(card1)
# pts2 = np.float32(card2)
ptsShow = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, ptsShow)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(img, (pts1[x][0], pts1[x][1]), 5, (0, 255, 0), cv2.FILLED)
    # cv2.circle(img, (pts2[x][0], pts2[x][1]), 5, (0, 255, 0), cv2.FILLED)

imgOutput = cv2.resize(imgOutput, (width, height))
img = cv2.resize(img, (550, 450))
cv2.imshow("Original Image ", img)
cv2.imshow("Output Image ", imgOutput)
cv2.waitKey(0)

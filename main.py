# # READ AND DISPLAY AN IMAGE
# import cv2
#
# img = cv2.imread('data/item.jpg')
#
# cv2.imshow('Img', img)
#
# cv2.waitKey(1000)

# READ AND SHOW VIDEO
# import cv2
# frameWidth = 1280
# frameHeight = 720
# # string for directory, 0 for webcam
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# while True:
#     success, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow('Video', img)
#


# EROSION/DILATION display and show with kernel
# import cv2
# import numpy as np
#
# kernel = np.ones((5, 5), np.uint8)
#
# path = 'data/item.jpg'
# img = cv2.imread(path)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(imgBlur, 100, 200)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
#
# cv2.imshow('Person', img)
# cv2.imshow('Gray Image', imgGray)
# cv2.imshow('Blur', imgBlur)
# cv2.imshow('Canny', imgCanny)
# cv2.imshow('Dilation', imgDilation)
# cv2.imshow('Erosion', imgErosion)
# cv2.waitKey(0)

# CROPPED, RESIZE IMAGE
# import cv2
#
# path = 'data/item.jpg'
# img = cv2.imread(path)
#
# width, height = 400, 600
# imgResize = cv2.resize(img, (width, height))
# print(imgResize.shape)
#
# imgCropped = img[0:900, 300:540]
# imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))
#
# cv2.imshow('Image', img)
# # cv2.imshow('Resized image', imgResize)
# cv2.imshow('Cropped Image', imgCropped)
# cv2.imshow('Cropped image Resize', imgCropResize)
# cv2.waitKey(0)

# DRAWING SHAPE
# import cv2
# import numpy as np
#
# img = np.zeros((512, 512, 3), np.uint8)
# # img[20:30, 60:100] = 255, 0, 0
# # img[:] = 255, 0, 0
#
# print(img)
#
# cv2.line(img, (0, 0), (img.shape[0], img.shape[1]), (0, 255, 0), 2)
# cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)
# cv2.circle(img, (150, 400), 50, (255, 0, 0), cv2.FILLED)
# cv2.putText(img, "Draw Shape", (75, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)
# cv2.imshow("Image", img)
# cv2.waitKey(0)

# MULTIPLE DISPLAY
# import cv2
# import numpy as np
#
# img1 = cv2.imread('data/item.jpg')
# img2 = cv2.imread('data/per.jpg')
# print(img1.shape)
# print(img2.shape)
#
# img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
# img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)
#
# horizontal = np.hstack((img1, img2))
# vertical = np.vstack((img1, img2))
#
# cv2.imshow('vertical', vertical)
# cv2.imshow('horizontal', horizontal)
# cv2.waitKey(0)

# MULTI DISPLAY
################### Stacking images without Function ################
# import cv2
# import numpy as np
# img1 = cv2.imread('data/item.jpg',0)
# img2 = cv2.imread('data/per.jpg')
# print(img1.shape)
# print(img2.shape)
# img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
# img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)
# img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
# hor= np.hstack((img1, img2))
# ver = np.vstack((img1, img2))
# cv2.imshow('Vertical', ver)
# cv2.imshow('Horizontal', hor)
# cv2.waitKey(0)
################### Stacking images WITH Function ################
# import cv2
# import numpy as np
#
# def stackImages(scale, imgArray):
#     rows = len(imgArray)
#     cols = len(imgArray[0])
#     rowsAvailable = isinstance(imgArray[0], list)
#     width = imgArray[0][0].shape[1]
#     height = imgArray[0][0].shape[0]
#     if rowsAvailable:
#         for x in range(0, rows):
#             for y in range(0, cols):
#                 if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
#                 else:
#                     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
#                                                 None, scale, scale)
#                 if len(imgArray[x][y].shape) == 2:
#                     imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
#         imageBlank = np.zeros((height, width, 3), np.uint8)
#         horizontal = [imageBlank] * rows
#         for x in range(0, rows):
#             horizontal[x] = np.hstack(imgArray[x])
#         vertical = np.vstack(horizontal)
#     else:
#         for x in range(0, rows):
#             if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
#                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
#             else:
#                 imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
#             if len(imgArray[x].shape) == 2:
#                 imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
#         horizontal = np.hstack(imgArray)
#         vertical = horizontal
#     return vertical
#
# kernel = np.ones((5, 5), np.uint8)
#
# path = 'data/item.jpg'
# img = cv2.imread(path)
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(imgBlur, 100, 200)
# imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgErosion = cv2.erode(imgDilation, kernel, iterations=1)
#
# stackImages = stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgDilation, imgErosion]))
# cv2.imshow('Stacked', stackImages)
#
# cv2.waitKey(0)
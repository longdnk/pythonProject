import cv2
import numpy as np

circles = np.zeros((4, 2), np.int)
counter = 0


def mousePoint(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        circles[counter] = x, y
        counter += 1


img = cv2.imread('data/chair.jpg')
while True:
    if counter == 4:
        # Tính toán kích thước của ảnh con
        card_width = np.abs(circles[1][0] - circles[0][0] + 1)
        card_height = np.abs(circles[2][1] - circles[0][1] + 1)
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        # pts2 = np.float32(card2)
        ptsShow = np.float32([[0, 0], [card_width, 0], [0, card_height], [card_width, card_height]])
        matrix = cv2.getPerspectiveTransform(pts1, ptsShow)
        imgOutput = cv2.warpPerspective(img, matrix, (card_width, card_height))
        imgResized = cv2.resize(imgOutput, (card_width + 100, card_height + 100))
        cv2.imshow('Output', imgResized)

    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 5, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mousePoint)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

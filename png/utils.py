import cv2
import numpy as np

#openCV 에서는 BGR 순으로 채널 지정
BLUE = 0
GREEN = 1
RED = 2
# 특정한 색상의 모든 단어가 포함된 이미지를 추출합니다.
def get_chars(image, color):
    other_1 = (color + 1) % 3
    other_2 = (color + 2) % 3

    c = image[:, :, other_1] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, other_2] == 255
    image[c] = [0, 0, 0]
    c = image[:, :, color] < 170
    image[c] = [0, 0, 0]
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255]
    return image


def leave_red(image, color):
    other_1 = (color + 1) % 3 #BLUE
    other_2 = (color + 2) % 3 #GREEN

    c = image[:, :, other_1] > 175 #BLUE
    image[c] = [0, 0, 0] #black
    c = image[:, :, other_2] > 175 #GREEN
    image[c] = [0, 0, 0]
    #c = image[:, :, color] < 170
    #image[c] = [0, 0, 0]
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255] #white
    return image

def leave_blue(image, color):
    other_1 = (color + 1) % 3 #GREEN
    other_2 = (color + 2) % 3 #RED

    c = image[:, :, other_1] > 180 #GREEN
    image[c] = [0, 0, 0] #black
    c = image[:, :, other_2] > 185 #RED
    image[c] = [0, 0, 0]
    c = image[:, :, color] > 200
    image[c] = [0, 0, 0]
    c = image[:, :, color] != 0
    image[c] = [255, 255, 255] #white
    return image


# 전체 이미지에서 왼쪽부터 단어별로 이미지를 추출합니다.
def extract_chars(image):
    chars = []
    #colors = [BLUE, GREEN, RED]
    colors = [RED]
    for color in colors:
        image_from_one_color = leave_red(image.copy(), color)
        image_gray = cv2.cvtColor(image_from_one_color, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image_gray, 127, 255, 0) #cv2.THRESH_BINARY

        # RETR_EXTERNAL 옵션으로 숫자의 외각을 기준으로 분리
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        # 추출된 이미지 크기가 50 이상인 경우만 실제 문자 데이터인 것으로 파악
        area = cv2.contourArea(contour)
        if area > 50:
            x, y, width, height = cv2.boundingRect(contour)
            roi = image_gray[y:y + height, x:x + width]
            chars.append((x, roi, area))

    chars = sorted(chars, key=lambda char: char[0])
    return chars


# 특정한 이미지를 (20 x 20) 크기로 Scaling 합니다.
def resize20(image):
    resized = cv2.resize(image, (20, 20))
    return resized.reshape(-1, 400).astype(np.float32)

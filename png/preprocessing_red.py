import cv2
import utils
import os

os.chdir('C:\\BrityDefault\\qoo10_captcha_data\\png\\red_img') #red_img 경로 지정
cur_path = os.getcwd()


for i in range(1,16):
    image = cv2.imread(str(i) + '.png', cv2.IMREAD_COLOR)

    #cv2.imshow('Origin Image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    red = utils.leave_red(image.copy(),utils.RED)
    #cv2.imshow('Image Gray', red)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    converted_path = 'C:\\BrityDefault\\qoo10_captcha_data\\png\\red_img\\converted'

    #배경이미지
    background = cv2.imread(converted_path + '\\background.png')

    #이미지 합치기
    h, w, c = red.shape
    background[50:50 + h, 150:150+w] = red #red 이미지를 background에 넣기
    cv2.imshow('img' , background)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite(converted_path + '\\' + str(i) + '_converted.png', background)
    print(str(i) + '_converted.png is successfully saved !')





#chars = utils.extract_chars(image.copy())
#for char in chars:
#    print('area : ' + str(char[2]))
#    cv2.imshow('image', char[1])
#    cv2.waitKey(0)


'''
blue = utils.get_chars(image.copy(), utils.BLUE)
green = utils.get_chars(image.copy(), utils.GREEN)
red = utils.get_chars(image.copy(), utils.RED)
cv2.imshow('Image Gray', blue)
cv2.waitKey(0)
cv2.imshow('Image Gray', green)
cv2.waitKey(0)
cv2.imshow('Image Gray', red)
cv2.waitKey(0)
'''



'''
original = cv2.imread('C:\\Users\\ASUS X571GT\\Desktop\\BSG ONE\\MOMENTSCOMPANY\\captcha5.jpg', cv2.IMREAD_COLOR)
gray = cv2.imread('C:\\Users\\ASUS X571GT\\Desktop\\BSG ONE\\MOMENTSCOMPANY\\captcha5.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original', original)
cv2.imshow('Gray', gray)

cv2.imwrite('C:\\Users\\ASUS X571GT\\Desktop\\BSG ONE\\MOMENTSCOMPANY\\captcha5_gray.jpg', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

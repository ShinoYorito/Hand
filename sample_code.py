import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 简单的读取图像函数
def imgload(path):
  img = cv2.imread(path) # 从路径中读取所需图片文件
  img = cv2.flip(img,1) #  翻转图像,使识别左右手结果正确
  img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 转换图像格式,openCv2读取图像结果为BGR,而mediapipe需要RGB图像
  return img

# 简单的图像显示函数
def imgshow(target):
  plt.imshow(target)
  plt.show()

img = imgload('./img.jpg')
# imgshow(img)

hand = mp_hands.Hands(
    static_image_mode=True, # 静态帧模式,True为图片处理,False为视频流处理
    max_num_hands=2, # 最大手部数量
    min_detection_confidence=0.5) # 置信度

result = hand.process(img)
# print(len(result.multi_hand_landmarks)) # 输出检测到手的个数,为1时会报错

# imgeread(img)
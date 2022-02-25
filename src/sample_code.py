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
  img = cv2.flip(img,1) #  水平翻转图像,使识别左右手结果正确
  img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 转换图像格式,openCv2读取图像结果为BGR,而mediapipe需要RGB图像
  return img

# 简单的图像显示函数
def imgshow(target):
  plt.imshow(target)
  plt.show()

img = imgload('./img.jpg')
# imgshow(img)

# 新建一个用于处理手部参数的图像处理器
hand = mp_hands.Hands(
    static_image_mode=True, # 静态帧模式,True为图片处理,False为视频流处理
    max_num_hands=2, # 最大手部数量
    min_detection_confidence=0.8, # 置信度,识别精准度随置信度提高,但识别率会随之降低
    min_tracking_confidence=0.8) # 追踪权重,权重越高追踪越准,但处理速度会降低

results = hand.process(img) # 对图像进行处理
# print(len(result.multi_hand_landmarks)) # 输出检测到手的个数,没有时会报错

if results.multi_hand_landmarks: # 若检测到手
  # 则获取每个手的参数
  for hand_idx in range(len(results.multi_hand_landmarks)):
    point = results.multi_hand_landmarks[hand_idx] # 获取每个手部的所有关键点坐标
    mp_drawing.draw_landmarks(img, point,mp_hands.HAND_CONNECTIONS) # 手部关键点绘制

imgshow(img)
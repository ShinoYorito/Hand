import os
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt

# 显示目标图像
def imgshow(target):
  plt.imshow(target)
  plt.show()

# 对既有Frame对图像进行处理
def imgloadbyframe(frame):
  frame = cv2.flip(frame, 1) # 水平翻转图像,使识别左右手结果正确
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)# 转换图像格式,openCv2读取图像结果为BGR,而mediapipe需要RGB图像
  return frame

# 通过路径读取图像并处理 
def imgloadbypath(path):
  try:
    img = cv2.imread(path) # 从路径中读取所需图片文件
    img = imgloadbyframe(img)
  except:
    print('Error object or not found :', path)
  else:
    return img

# 处理图像函数
def process(frame, solution, processor):
  results = processor.process(frame) # 使用被实例化的处理器 对图像进行处理
  if results.multi_hand_landmarks: # 若检测到手
    mp_drawing = mp.solutions.drawing_utils # 调用默认绘制工具
    # 则获取每个手的参数
    for hand_idx in range(len(results.multi_hand_landmarks)):
      point = results.multi_hand_landmarks[hand_idx] # 获取每个手部的所有关键点坐标
      mp_drawing.draw_landmarks(frame, point,solution.HAND_CONNECTIONS) # 手部关键点绘制
  return frame

def sample(path):
  mp_hands = mp.solutions.hands # 实例化Hands解决方案
  hand = mp_hands.Hands( # 实例化一个用于处理手部参数的图像处理器
    static_image_mode=True, # 静态帧模式,True为图片处理,False为视频流处理
    max_num_hands=2, # 最大手部数量
    min_detection_confidence=0.6, # 置信度,识别精准度随置信度提高,但识别率会随之降低
    min_tracking_confidence=0.6) # 追踪权重,权重越高追踪越准,但处理速度会降低
  
  img = imgloadbypath(path)
  process(img,mp_hands,hand)
  imgshow(img)


sample("./src/img.jpg") # 单张图像处理示范
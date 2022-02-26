import os
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands # 实例化Hands解决方案
hand = mp_hands.Hands( # 实例化一个用于处理手部参数的图像处理器
  static_image_mode=False, # 静态帧模式,True为图片处理,False为视频流处理
  max_num_hands=2, # 最大手部数量
  min_detection_confidence=0.7, # 置信度,识别精准度随置信度提高,但识别率会随之降低
  min_tracking_confidence=0.6) # 追踪权重,权重越高追踪越准,但处理速度会降低

cap = cv2.VideoCapture(0) # 占用视频流(相机) 为0为默认摄像头

finger = [0,0,0,0,0,0]

while cap.isOpened():
    success, frame = cap.read() # 读取camera内容
    if not success:
        print("ERROR: Open Camera Failed!")
        continue
    else:
        cv2.flip(frame, 1)
        results = hand.process(frame)
        # print(results.multi_handedness)
    if (results.multi_handedness != None):
        for i in range(1,6):
            # 指根与指尖的净距离
            xraw = pow((results.multi_hand_landmarks[0].landmark[0].x - results.multi_hand_landmarks[0].landmark[i*4].x),2)
            yraw = pow((results.multi_hand_landmarks[0].landmark[0].y - results.multi_hand_landmarks[0].landmark[i*4].y),2)
            zraw = pow((results.multi_hand_landmarks[0].landmark[0].z - results.multi_hand_landmarks[0].landmark[i*4].z),2)
            
            # 指根与第一指节的距离 用于降低手与摄像头距离带来的影响
            xp = pow((results.multi_hand_landmarks[0].landmark[0].x - results.multi_hand_landmarks[0].landmark[(i*4) - 3].x),2)
            yp = pow((results.multi_hand_landmarks[0].landmark[0].y - results.multi_hand_landmarks[0].landmark[(i*4) - 3].y),2)
            zp = pow((results.multi_hand_landmarks[0].landmark[0].z - results.multi_hand_landmarks[0].landmark[(i*4) - 3].z),2)

            # 求出指尖坐标与指跟坐标距离 除以指根与第一指节的距离 减轻摄像头与手之间的距离变化造成的影响
            dist = (pow((xraw + yraw + zraw), 0.5) / pow((xp + yp + zp), 0.5)) 
            
            # 补偿值，因个体差异 补偿值可能不同
            # 拇指 - 2.5  食指 - 0.8  中指 - 0.6  无名指 - 0.6  尾指 - 0.6
            if i == 1:
                dist = abs(dist - 2.5)
            elif i == 2:
                dist = abs(dist - 0.8)
            elif i == 3:
                dist = abs(dist - 0.7)
            elif i == 4:
                dist = abs(dist - 0.6)
            elif i == 5:
                dist = abs(dist - 0.6)
            if dist > 1:
                dist = 1
            finger[i] = round(dist, 2) # 放入finger中 (第0个为指跟坐标)
        print(finger)

cap.release() # 解除摄像头占用



import cv2
import mediapipe as mp
import math
import serial
import copy
import output
import matplotlib.pyplot as plt
import numpy
mp_drawing_styles = mp.solutions.drawing_styles
com = output.init('COM4', 9600)
def vector_2d_angle(v1, v2):
    '''
        求解二维向量的角度
    '''
    v1_x = v1[0]
    v1_y = v1[1]
    v2_x = v2[0]
    v2_y = v2[1]
    try:
        angle_ = math.degrees(math.acos(
            (v1_x * v2_x + v1_y * v2_y) / (((v1_x ** 2 + v1_y ** 2) ** 0.5) * ((v2_x ** 2 + v2_y ** 2) ** 0.5))))
    except:
        angle_ = 65535.
    if angle_ > 180.:
        angle_ = 65535.
    return angle_


def hand_angle(hand_):
    '''
        获取对应手相关向量的二维角度,根据角度确定手势
    '''
    angle_list = []
    # ---------------------------- thumb 大拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[2][0])), (int(hand_[0][1]) - int(hand_[2][1]))),
        ((int(hand_[3][0]) - int(hand_[4][0])), (int(hand_[3][1]) - int(hand_[4][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- index 食指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[6][0])), (int(hand_[0][1]) - int(hand_[6][1]))),
        ((int(hand_[7][0]) - int(hand_[8][0])), (int(hand_[7][1]) - int(hand_[8][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- middle 中指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[10][0])), (int(hand_[0][1]) - int(hand_[10][1]))),
        ((int(hand_[11][0]) - int(hand_[12][0])), (int(hand_[11][1]) - int(hand_[12][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- ring 无名指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[14][0])), (int(hand_[0][1]) - int(hand_[14][1]))),
        ((int(hand_[15][0]) - int(hand_[16][0])), (int(hand_[15][1]) - int(hand_[16][1])))
    )
    angle_list.append(angle_)
    # ---------------------------- pink 小拇指角度
    angle_ = vector_2d_angle(
        ((int(hand_[0][0]) - int(hand_[18][0])), (int(hand_[0][1]) - int(hand_[18][1]))),
        ((int(hand_[19][0]) - int(hand_[20][0])), (int(hand_[19][1]) - int(hand_[20][1])))
    )
    angle_list.append(angle_)
    return angle_list


def jiexian(num):
    if num > 2000:
        return 2000
    elif num < 0:
        return 0
    else:
        return int(num)


def hex_ten(str):
    if '0' <= str <= '9':
        return int(str)
    elif str == 'a':
        return 10
    elif str == 'b':
        return 11
    elif str == 'c':
        return 12
    elif str == 'd':
        return 13
    elif str == 'e':
        return 14
    elif str == 'f':
        return 15


def h_gesture(angle_list):
    '''
        # 二维约束的方法定义手势
        # fist five gun love one six three thumbup yeah
    '''
    thr_angle = 65.
    thr_angle_thumb = 53.
    thr_angle_s = 49.
    gesture_str = None
    if 65535. not in angle_list:
        # print(angle_list)
        hand_list = []
        hand_list.append(jiexian(angle_list[0] * 20))
        hand_list.append(jiexian(2000 - angle_list[1] * 12))
        hand_list.append(jiexian(2000 - angle_list[2] * 12))
        hand_list.append(jiexian(2000 - angle_list[3] * 12))
        hand_list.append(jiexian(2000 - angle_list[4] * 12))
        print(hand_list)
        output.full_motor_action(com, hand_list)  # 将动作发送至串口 不需要手腕坐标

        if (angle_list[0] > thr_angle_thumb) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "fist"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle_s):
            gesture_str = "five"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "gun"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "love"
        elif (angle_list[0] > 5) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "one"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "six"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] > thr_angle):
            gesture_str = "three"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "thumbUp"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "two"
    return gesture_str


def inbuffer(angle_input, buffer, buffersize = 5):
    print("Buffer in\n", buffer)
    print("-------------------------------", angle_input)
    angle_output = [] # 构建一个输出Angle

    # 将输入的五个指头分别存入各自的buffer
    buffer = buffer.tolist() # 转为List便于操作
    buffer.pop() # Pop出最先放入的Angle
    buffer.insert(0, angle_input) # Push 入一个angle
    buffer = numpy.array(buffer)# 转回array

    # 进行Angle 均值计算
    buffer = numpy.rot90(buffer,3) # 旋转90度用于计算逐个指头的角度
    for i in buffer:
        print("Buffer: ", i)
        print("Mean: ", numpy.mean(i))
        angle_output.append(numpy.mean(i))
    buffer= numpy.rot90(buffer) # 进行3次旋转以复原矩阵
    
    print("++++++++++++++++++++++++++++++++", angle_output)
    return angle_output, buffer


def moving_average(interval, windowsize):
    window = numpy.ones(int(windowsize)) / float(windowsize)
    re = numpy.convolve(interval, window, 'same')
    return re

def detect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75)
    cap = cv2.VideoCapture(0)
    buffersize = 5    # 生成一个Buffersize行,5列的数组
    buffer = numpy.ones((buffersize, 5))
    while True:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)
        results = hands.process(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing_styles.get_default_hand_landmarks_style(),
                                          mp_drawing_styles.get_default_hand_connections_style())
                hand_local = []
                for i in range(21):
                    x = hand_landmarks.landmark[i].x * frame.shape[1]
                    y = hand_landmarks.landmark[i].y * frame.shape[0]
                    hand_local.append((x, y))
                if hand_local:
                    angle_list = hand_angle(hand_local)

                    before.append(angle_list[0])   # 原始数据存进before
                    x_raw.append(len(before))      # plt的x轴

                    angle_list1 = moving_average(angle_list, 10)
                    angle_list2,buffer = inbuffer(angle_list, buffer, buffersize)

                    after.append(angle_list1[0])    # 处理后的数据存进after
                    after2.append(angle_list2[0])    # 处理后的数据存进after
                    

                    gesture_str = h_gesture(angle_list2)
                    cv2.putText(frame, gesture_str, (0, 100), 0, 1.3, (0, 0, 255), 3)
        cv2.imshow('MediaPipe Hands', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()

    plt.title("Fingers",fontsize = 24)
    plt.xlabel("time",fontsize = 14)
    plt.ylabel("Args",fontsize = 14)

    plt.plot(x_raw,before,linewidth=1,label='before')
    plt.plot(x_raw,after,linewidth=1,label='after')
    plt.plot(x_raw,after2,linewidth=1,label='after2')
    plt.legend()

    tick = numpy.arange(stop=len(x_raw),step=10)
    plt.xticks(tick)
    plt.tick_params(axis='both',labelsize = 14)
    plt.show()
    


if __name__ == '__main__':
    
    before = []
    after = []
    after2 = []
    x_raw = []
    detect()

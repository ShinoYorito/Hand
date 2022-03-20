import math
import threading
import mediapipe as mp
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import *
import cv2 as cv
import numpy as np
mp_drawing_styles = mp.solutions.drawing_styles

uipath = "src\sysui.ui"
def thread_runner(func):
    """多线程装饰器"""

    def wrapper(*args, **kw):
        print(f'Start new thread: {func.__name__}')
        threading.Thread(target=func, args=args, kwargs=kw).start()

    return wrapper


def jiexian(num):
    if num > 2000:
        return 2000
    elif num < 0:
        return 0
    else:
        return int(num)
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
        #output.full_motor_action(com, hand_list)  # 将动作发送至串口 不需要手腕坐标

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

class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(uipath)
        # 动态加载整个ui

        self.ui.camButton.clicked.connect(self.cam_Button)
        # 把[camButton]这个按钮的点击连接到cam_Button函数

        self.ui.handconnectButton.clicked.connect(self.handconnect_Button)
        # 把[handconnectButton]这个按钮的点击连接到handconnect_Button函数

        self.ui.numbermodeChoice.clicked.connect(self.numbermode_Choice)
        # 把[numbermodeChoice]这个按钮的点击连接到numbermode_Choice函数

        self.ui.followmodeChoice.clicked.connect(self.followmode_Choice)
        # 把[followmodeChoice]这个按钮的点击连接到followmode_Choice函数

        self.ui.gamblemodeChoice.clicked.connect(self.gamblemode_Choice)
        # 把[gamblemodeChoice]这个按钮的点击连接到gamblemode_Choice函数

        self.ui.youwinBox.clicked.connect(self.youwin_Box)
        # 把[youwinBox]这个按钮的点击连接到youwin_Box函数
        self.ui.youwinBox.setEnabled(self.ui.gamblemodeChoice.isChecked())
        # 语音播报的选择状态跟随划拳按钮

        self.ui.onemoreThing.clicked.connect(self.onemore_Thing)
        # 把[onemoreThing]这个按钮的点击连接到onemore_Thing函数


        # ---------------------以下为五指选择框模块定义------------------------- #
        self.ui.xiaozhiCheck.clicked.connect(self.xiaozhi_Check)
        self.ui.wumingzhiCheck.clicked.connect(self.wumingzhi_Check)
        self.ui.zhongzhiCheck.clicked.connect(self.zhongzhi_Check)
        self.ui.shizhiCheck.clicked.connect(self.shizhi_Check)
        self.ui.muzhiCheck.clicked.connect(self.muzhi_Check)
        # ---------------------以上为五指选择框模块定义------------------------- #


        # ---------------------以下为五指调节模块定义---------------------------- #
        self.ui.xiaozhiSlider.valueChanged[int].connect(self.xiaozhi_Tiaojie)
        self.ui.wumingzhiSlider.valueChanged[int].connect(self.wumingzhi_Tiaojie)
        self.ui.zhongzhiSlider.valueChanged[int].connect(self.zhongzhi_Tiaojie)
        self.ui.shizhiSlider.valueChanged[int].connect(self.shizhi_Tiaojie)
        self.ui.muzhiSlider.valueChanged[int].connect(self.muzhi_Tiaojie)
        # ---------------------以上为五指调节模块定义---------------------------- #


        # ------------------------以下为数字按键模块定义----------------- #
        self.ui.num0Button.clicked.connect(self.num0_Button)
        self.ui.num1Button.clicked.connect(self.num1_Button)
        self.ui.num2Button.clicked.connect(self.num2_Button)
        self.ui.num3Button.clicked.connect(self.num3_Button)
        self.ui.num4Button.clicked.connect(self.num4_Button)
        self.ui.num5Button.clicked.connect(self.num5_Button)
        self.ui.num6Button.clicked.connect(self.num6_Button)
        self.ui.num7Button.clicked.connect(self.num7_Button)
        self.ui.num8Button.clicked.connect(self.num8_Button)
        self.ui.num9Button.clicked.connect(self.num9_Button)
        # 9个按键都连接到对应的函数
        # ------------------------以上为数字按键模块定义----------------- #


#------------------------------下面是函数----------------------------------#


    # --------------------以下为手指选择功能逻辑------------------ #
    def xiaozhi_Check(self):
        if self.ui.xiaozhiCheck.isChecked() == True:
            print("小指选中了")
        else:
            print("小指取消选中了")

    def wumingzhi_Check(self):
        if self.ui.wumingzhiCheck.isChecked() == True:
            print("无名指选中了")
        else:
            print("无名指取消选中了")

    def zhongzhi_Check(self):
        if self.ui.zhongzhiCheck.isChecked() == True:
            print("中指选中了")
        else:
            print("中指取消选中了")

    def shizhi_Check(self):
        if self.ui.shizhiCheck.isChecked() == True:
            print("食指选中了")
        else:
            print("食指取消选中了")

    def muzhi_Check(self):
        if self.ui.muzhiCheck.isChecked() == True:
            print("拇指选中了")
        else:
            print("拇指取消选中了")
    # --------------------以上为手指选择功能逻辑------------------ #


    # --------------------以下为手指调节功能逻辑------------------ #
    def xiaozhi_Tiaojie(self):
        xiaozhi_jiaodu = self.ui.xiaozhiSlider.value()
        print("小指调节程度为" + str(xiaozhi_jiaodu) + "%")

    def wumingzhi_Tiaojie(self):
        wumingzhi_jiaodu = self.ui.wumingzhiSlider.value()
        print("无名指调节程度为" + str(wumingzhi_jiaodu) + "%")

    def zhongzhi_Tiaojie(self):
        zhongzhi_jiaodu = self.ui.zhongzhiSlider.value()
        print("中指调节程度为" + str(zhongzhi_jiaodu) + "%")

    def shizhi_Tiaojie(self):
        shizhi_jiaodu = self.ui.shizhiSlider.value()
        print("食指调节程度为" + str(shizhi_jiaodu) + "%")

    def muzhi_Tiaojie(self):
        muzhi_jiaodu = self.ui.muzhiSlider.value()
        print("拇指调节程度为" + str(muzhi_jiaodu) + "%")
    # --------------------以上为手指调节功能逻辑------------------ #


    def gesture_Text(self, shuruTXT):
        self.ui.gestureText.setText(shuruTXT)
        print("手势上屏文字显示为:" + shuruTXT)

    @thread_runner
    def cam_Button(self):
        # 显示摄像头画面
        print("单击以 开始|结束 摄像头画面")
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.75,
            min_tracking_confidence=0.75)
        cap = cv.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = cv.flip(frame, 1)
            results = hands.process(frame)
            frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)

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
                        gesture_str = h_gesture(angle_list)
                        cv.putText(frame, gesture_str, (0, 100), 0, 1.3, (0, 0, 255), 3)
            show = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
            self.ui.camWindow.setPixmap(QPixmap.fromImage(frame))
            if cv.waitKey(1) & 0xFF == 27:
                break
        




    def handconnect_Button(self):
        # 连接机械手掌
        print("单击以 连接|断开 机械手掌")

    def followmode_Choice(self):
        # 进入手势跟随模式
        print("手势跟随模式已经打开了")

    def gamblemode_Choice(self):
        # 进入划拳模式
        print("人机猜拳模式已经打开了")
        self.ui.youwinBox.setEnabled(1)
        # 语音播报可以选择了

    def youwin_Box(self):
        # 划拳模式打开语音播报
        if self.ui.gamblemodeChoice.isChecked() == True:
            self.ui.youwinBox.setEnabled(self.ui.gamblemodeChoice.isChecked())
        # 语音播报的选择状态跟随划拳按钮
        else:
            print("先开划拳模式")
            self.ui.youwinBox.setEnabled(0)  # 不能按

    def onemore_Thing(self):
        # 清空所有模式
        print("清空所有模式")


    # -----------------------以下为数字按键模块功能逻辑---------------------- #
    def numbermode_Choice(self):
        # 进入数字手势模式
        print("数字手势模式已经打开了")


    def num0_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:0")
        else:
            print("数字0按了没用")

    def num1_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:1")
        else:
            print("数字1按了没用")

    def num2_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:2")
        else:
            print("数字2按了没用")

    def num3_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:3")
        else:
            print("数字3按了没用")

    def num4_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:4")
        else:
            print("数字4按了没用")

    def num5_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:5")
        else:
            print("数字5按了没用")

    def num6_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:6")
        else:
            print("数字6按了没用")

    def num7_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:7")
        else:
            print("数字7按了没用")

    def num8_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:8")
        else:
            print("数字8按了没用")

    def num9_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:9")
        else:
            print("数字9按了没用")
    # -----------------------以上为数字按键模块功能逻辑---------------------- #



app = QApplication([])          # QApplication 提供了整个图形界面程序的底层管理功能
stats = Stats()                 # 调用Stats这个类
stats.gesture_Text("Testing")      # 测试上屏手势显示文字
stats.ui.show()                 # 放在主窗口的控件，要能全部显示show在界面上
app.exec_()                     # 进入QApplication的事件处理循环
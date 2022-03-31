import math
import output
import threading
import mediapipe as mp
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import *
import cv2
import numpy as np
import time


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
    elif num < 900:
        return 900
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

def timer():
    while(stats.dtime):
        time.sleep(1)
        stats.dtime = stats.dtime - 1
    stats.denable = ~stats.denable
    
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
        if (angle_list[0] > thr_angle_thumb) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "拳头"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle_s):
            gesture_str = "五|布"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "八|手枪"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "比心"
        elif (angle_list[0] > 5) and (angle_list[1] < thr_angle_s) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "一"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] < thr_angle_s):
            gesture_str = "六"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] > thr_angle):
            gesture_str = "三"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] < thr_angle_s) and (angle_list[4] < thr_angle):
            gesture_str = "四"
        elif (angle_list[0] < thr_angle_s) and (angle_list[1] > thr_angle) and (angle_list[2] > thr_angle) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "点赞"
        elif (angle_list[0] > thr_angle_thumb) and (angle_list[1] < thr_angle_s) and (angle_list[2] < thr_angle_s) and (
                angle_list[3] > thr_angle) and (angle_list[4] > thr_angle):
            gesture_str = "二|剪刀"
        
        # print(hand_list)
        if (stats.working_mode == 2):  # 跟随模式
            output.full_motor_action(stats.com, hand_list)  # 将动作发送至串口 不需要手腕坐标
    return gesture_str


def detect():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.75,
        min_tracking_confidence=0.75)
    cap = cv2.VideoCapture(0)
    gesture_str = '未定义的手势'
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
                    gesture_str = h_gesture(angle_list)
        if (stats.working_mode == 3):# 猜拳模式
            if (stats.denable):
                if (stats.dtime):
                    if stats.dtime == 1:
                        cv2.putText(frame, 'start!', (30, 350), 0, 7, (255, 255, 0), 15)
                    else:
                        cv2.putText(frame, str(stats.dtime-1), (130, 410), 0,15, (255, 255, 0), 15)
                else:
                    print("Enterd Gamble Mode")
                    stats.dtime = 4 # sec
                    gbl = threading.Thread(target=timer)
                    gbl.start()
        show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)
        stats.gesture_Text(gesture_str)
        stats.cam_Disp(frame)
        if ~Stats.cam_status or cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()

class Stats:
    cam_status = 0  # 摄像头模式开关
    working_mode = 0 # 设备运行模式 0为清空,1为数字手势,2为手部跟随,3为划拳,4为动作录制
    hand_enable = 0 # 手部功能总开关
    dtime = 0 # 猜拳模式计时器
    denable = 0 # 猜拳模式开关 按下后打开     
    com = None
    def __init__(self):
        # 从文件中加载UI定义
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(uipath)
        # 动态加载整个ui
        self.check_state = []

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

        self.gesture_Text(Window_text)      # 初始化手势显示文字

#------------------------------下面是函数----------------------------------#

# --------------------以下为手指选择功能逻辑------------------ #
    def xiaozhi_Check(self):
        try:
            if self.ui.xiaozhiCheck.isChecked() == True:
                self.check_state.append(self.ui.xiaozhiSlider)
            else:
                self.check_state.remove(self.ui.xiaozhiSlider)
        except:
            pass

    def wumingzhi_Check(self):
        try:
            if self.ui.wumingzhiCheck.isChecked() == True:
                self.check_state.append(self.ui.wumingzhiSlider)
            else:
                self.check_state.remove(self.ui.wumingzhiSlider)
        except:
            pass

    def zhongzhi_Check(self):
        try:
            if self.ui.zhongzhiCheck.isChecked() == True:
                self.check_state.append(self.ui.zhongzhiSlider)
            else:
                self.check_state.remove(self.ui.zhongzhiSlider)
        except:
            pass

    def shizhi_Check(self):
        try:
            if self.ui.shizhiCheck.isChecked() == True:
                self.check_state.append(self.ui.shizhiSlider)
            else:
                self.check_state.remove(self.ui.shizhiSlider)
        except:
            pass

    def muzhi_Check(self):
        try:
            if self.ui.muzhiCheck.isChecked() == True:
                self.check_state.append(self.ui.muzhiSlider)
            else:
                self.check_state.remove(self.ui.muzhiSlider)
        except:
            pass
    # --------------------以上为手指选择功能逻辑------------------ #


    # --------------------以下为手指调节功能逻辑------------------ #
    def xiaozhi_Tiaojie(self):
        xiaozhi_jiaodu = self.ui.xiaozhiSlider.value()
        if self.ui.xiaozhiSlider in self.check_state:
            for i in self.check_state:
                i.setValue(xiaozhi_jiaodu)
        arg = 900 + (xiaozhi_jiaodu * 11) # 将获取到的整形百分比 转为900~2000的有效值
        output.send_cmd(self.com, output.protoco(ctx = {5:arg}))

    def wumingzhi_Tiaojie(self):
        wumingzhi_jiaodu = self.ui.wumingzhiSlider.value()
        if self.ui.wumingzhiSlider in self.check_state:
            for i in self.check_state:
                i.setValue(wumingzhi_jiaodu)
        arg = 900 + (wumingzhi_jiaodu * 11) # 将获取到的整形百分比 转为900~2000的有效值
        output.send_cmd(self.com, output.protoco(ctx = {4:arg}))

    def zhongzhi_Tiaojie(self):
        zhongzhi_jiaodu = self.ui.zhongzhiSlider.value()
        if self.ui.zhongzhiSlider in self.check_state:
            for i in self.check_state:
                i.setValue(zhongzhi_jiaodu)
        arg = 900 + (zhongzhi_jiaodu * 11) # 将获取到的整形百分比 转为900~2000的有效值
        output.send_cmd(self.com, output.protoco(ctx = {3:arg}))

    def shizhi_Tiaojie(self):
        shizhi_jiaodu = self.ui.shizhiSlider.value()
        if self.ui.shizhiSlider in self.check_state:
            for i in self.check_state:
                i.setValue(shizhi_jiaodu)
        arg = 900 + (shizhi_jiaodu * 11) # 将获取到的整形百分比 转为900~2000的有效值
        output.send_cmd(self.com, output.protoco(ctx = {2:arg}))

    def muzhi_Tiaojie(self):
        muzhi_jiaodu = self.ui.muzhiSlider.value()
        if self.ui.muzhiSlider in self.check_state:
            for i in self.check_state:
                i.setValue(muzhi_jiaodu)
        arg = 2000 - (muzhi_jiaodu * 11) # 将获取到的整形百分比 转为900~2000的有效值 注意大拇指运作方向与其他四指相反
        output.send_cmd(self.com, output.protoco(ctx = {1:arg}))
    # --------------------以上为手指调节功能逻辑------------------ #


    def gesture_Text(self, shuruTXT):
        if (shuruTXT):
            self.ui.gestureText.setText(shuruTXT)

    def cam_Button(self):
        # 显示摄像头画面
        Stats.cam_status = ~Stats.cam_status # 线程控制开关
        if (Stats.cam_status):
            cam = threading.Thread(target = detect) # 创建子线程
            cam.start()
    
    def cam_Disp(self, Frame = None):
        if (Frame != None):
            self.ui.camWindow.setPixmap(QPixmap.fromImage(Frame))

    def handconnect_Button(self, port = 'COM6', baut = 9600):
        Stats.hand_enable = ~Stats.hand_enable
        arr_red = '''color: black; background-color: rgb(240, 128, 128)'''
        arr_green = '''color: black; background-color: rgb(152, 251, 152)'''
        # 连接机械手掌
        if (Stats.hand_enable):
            self.com = output.init(port, baut)
            if (self.com == -1):
                print("Failed to Open Com port")
                Stats.hand_enable = ~Stats.hand_enable
                self.ui.xiaozhiState.setStyleSheet(arr_red)
                self.ui.wumingzhiState.setStyleSheet(arr_red)
                self.ui.zhongzhiState.setStyleSheet(arr_red)
                self.ui.shizhiState.setStyleSheet(arr_red)
                self.ui.muzhiState.setStyleSheet(arr_red)
            else:
                self.ui.xiaozhiState.setStyleSheet(arr_green)
                self.ui.wumingzhiState.setStyleSheet(arr_green)
                self.ui.zhongzhiState.setStyleSheet(arr_green)
                self.ui.shizhiState.setStyleSheet(arr_green)
                self.ui.muzhiState.setStyleSheet(arr_green)
                return self.com
        else:
            output.free(self.com)
            print("Com port Closed")
            self.ui.xiaozhiState.setStyleSheet(arr_red)
            self.ui.wumingzhiState.setStyleSheet(arr_red)
            self.ui.zhongzhiState.setStyleSheet(arr_red)
            self.ui.shizhiState.setStyleSheet(arr_red)
            self.ui.muzhiState.setStyleSheet(arr_red)
            return 0

    def followmode_Choice(self):
        # 进入手势跟随模式
        self.working_mode = 2

    def gamblemode_Choice(self):
        # 进入划拳模式
        self.working_mode = 3
        self.denable = ~self.denable
        self.ui.youwinBox.setEnabled(1)
        # 语音播报可以选择了

    def youwin_Box(self):
        # 划拳模式打开语音播报
        if self.ui.gamblemodeChoice.isChecked() == True:
            self.ui.youwinBox.setEnabled(self.ui.gamblemodeChoice.isChecked())
        # 语音播报的选择状态跟随划拳按钮
        else:
            print("没有进入划拳模式")
            self.ui.youwinBox.setEnabled(0)  # 不能按

    def onemore_Thing(self):
        # 清空所有模式
        print("清空所有模式")
        self.working_mode = 0


    # -----------------------以下为数字按键模块功能逻辑---------------------- #
    def numbermode_Choice(self):
        # 进入数字手势模式
        self.working_mode = 1


    def num0_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:0")
            output.send_cmd(self.com, output.protoco(act="run", idx=0))
        else:
            print("数字0按了没用")

    def num1_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:1")
            output.send_cmd(self.com, output.protoco(act="run", idx=1))
        else:
            print("数字1按了没用")

    def num2_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:2")
            output.send_cmd(self.com, output.protoco(act="run", idx=2))
        else:
            print("数字2按了没用")

    def num3_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            print("数字手势:3")
            output.send_cmd(self.com, output.protoco(act="run", idx=3))
        else:
            print("数字3按了没用")

    def num4_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=4))
            print("数字手势:4")
        else:
            print("数字4按了没用")

    def num5_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=5))
            print("数字手势:5")
        else:
            print("数字5按了没用")

    def num6_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=6))
            print("数字手势:6")
        else:
            print("数字6按了没用")

    def num7_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=7))
            print("数字手势:7")
        else:
            print("数字7按了没用")

    def num8_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=8))
            print("数字手势:8")
        else:
            print("数字8按了没用")

    def num9_Button(self):
        if self.ui.numbermodeChoice.isChecked() == True:
            output.send_cmd(self.com, output.protoco(act="run", idx=9))
            print("数字手势:9")
        else:
            print("数字9按了没用")
    # -----------------------以上为数字按键模块功能逻辑---------------------- #


if __name__ == '__main__':
    mp_drawing_styles = mp.solutions.drawing_styles
    Window_text = '单击以开始屏幕显示'
    uipath = "src/sysui.ui"
    app = QApplication([])          # QApplication 提供了整个图形界面程序的底层管理功能
    stats = Stats()                 # 调用Stats这个类
    stats.ui.show()                 # 放在主窗口的控件，要能全部显示show在界面上
    app.exec_()                     # 进入QApplication的事件处理循环
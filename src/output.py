import serial

def protoco(ctx, head = [0x55, 0x55], act = [0x03], time = 0):
    # ctx : 报文内容,一个由舵机ID、角度构建的字典
    # time: 通过转动时间控制速度, 16进制 高低八位翻转 0~2000 (ms)
    # head: 报文头 协议规定0x55
    # act: 03-运转舵机 06-执行已经写入的动作组 07-停止动作 08-擦除已写入的动作组 17-写入一个动作组 
    
    time = [time & 0x00ff, (time & 0xff00) >> 8] # 按协议存放报文
    
    cnt = [] # 将舵机控制数构建为一个空列表
    size = [] # 将报文大小构建为一个空列表
    tail = [] # 将报文构建为一个空列表

    cnt.append(len(ctx.keys())) # 获得试图控制的舵机个数

    
    # 构建报文内容
    for item in ctx.keys():
        tail.append(int(item)) # 放入需要控制的舵机ID
        arg = int(ctx[item] * 2000) # 获得报文角度 (0~1)->(0~180°)
        arg = [arg & 0x00ff, (arg & 0xff00) >> 8] # 按协议存放报文
        tail = tail + arg # 放入对应舵机的动作角度
    
    size.append(len(act + cnt + time + tail) + 1) # 计算协议报文长度 加上自身长度
    return head + size + act + cnt + time + tail # 返回构建好的列表

# 初始化一个串口, port为COM口号，baut为波特率
def init(port, baut):
    com = serial.Serial(port, baut)
    return com

# 以字符形式发送命令
def send_cmd(dev, cmd): 
    print(cmd) # 打印日志 用于调试
    if dev.isOpen():
        dev.write(bytes(cmd))# 将内容发送至串口
    else:
        print("Open device Fail")

def full_motor_action(com, finger_index):
    finger = {} # 构建舵机:角度的字典
    cnt = 1 # 计数作为ID
    for i in finger_index:
        finger[cnt] = i
        cnt = cnt + 1
    send_cmd(com, protoco(finger))

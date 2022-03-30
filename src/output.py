import serial

# 03-运转舵机 06-执行已经写入的动作组 07-停止动作 08-擦除已写入的动作组 17-写入一个动作组
Act = {"exe":[0x03],"run":[0x06],"save":[0x17],"del":[0x08],"stop":[0x07]}


def protoco(head = [0x55, 0x55], act = "exe", ctx = {1:900,2:900,3:900,4:900,5:900}, spd = 0, idx = 1, time = 1):
    # head: 报文头 协议规定0x55 0x55
    # act: 需要执行的动作
    # ctx : 报文内容,一个0由舵机ID、角度构建的字典
    # spd: 通过转动时间控制速度, 16进制 高低八位翻转 0~2000 (ms)
    # idx：动作组运行时需要的参数,用于指定动作组
    # time: 运行次数，在执行动作组时会用到

    act = Act.get(act) # 将获取到的动作转为报文
    cnt = [] # 将舵机控制数构建为一个空列表
    size = [] # 将报文大小构建为一个空列表
    tail = [] # 将报文构建为一个空列表

    # 不同命令执行不同动作,报文不同

    # 直接执行动作报文
    if (Act.get("exe") == act):
        spd = [spd & 0x00ff, (spd & 0xff00) >> 8] # 按协议存放报文
        cnt.append(len(ctx.keys())) # 获得试图控制的舵机个数
        # 构建报文内容
        for item in ctx.keys():
            tail.append(int(item)) # 放入需要控制的舵机ID
            arg = int(ctx[item]) # 获得报文角度 (0~1)->(0~180°)
            arg = [arg & 0x00ff, (arg & 0xff00) >> 8] # 按协议存放报文
            tail = tail + arg # 放入对应舵机的动作角度
        
        size.append(len(act + cnt + spd + tail) + 1) # 计算协议报文长度 加上自身长度
        return head + size + act + cnt + spd + tail # 返回构建好的列表
        # 动作组 运行/擦除报文
    
    # 保存动作组
    elif (Act.get("save") == act):
        idx = [idx] # 将动作组转为16进制 并用元组保存
        time = [time & 0x00ff, (time & 0xff00) >> 8] # 保存运行次数
        cnt.append(len(ctx.keys())) # 获得试图控制的舵机个数
        spd = [spd & 0x00ff, (spd & 0xff00) >> 8] # 按协议存放报文
        for item in ctx.keys():
            tail.append(int(item)) # 放入需要控制的舵机ID
            arg = int(ctx[item]) # 获得报文角度 (0~1)->(0~180°)
            arg = [arg & 0x00ff, (arg & 0xff00) >> 8] # 按协议存放报文
            tail = tail + arg # 放入对应舵机的动作角度

        size.append(len(head + act + [1] + idx + time + cnt + spd + tail)) # 计算协议报文长度 加上自身长度
        
        # print("head ",head, "act ",act, "size ", size,"idx ",idx,"cnt",cnt, "spd", spd ,"tail ", tail)
        return head + act + size + idx + time + cnt + spd + tail

    # 动作组 运行/擦除报文
    elif (Act.get("run") == act or Act.get("del") == act):
        idx = [idx] # 将动作组转为16进制 并用元组保存
        time = [time & 0x00ff, (time & 0xff00) >> 8]
        size.append(len(act + idx + time) + 1) # 计算协议报文长度 加上自身长度
        return head + size + act + idx + time

    # 设备停止报文
    elif (act == Act.get("stop")):
        size.append(len(act) + 1)
        return head + size + act

    # 无法识别的报文
    else :
        print("Error Occured cause unrecongnized Protoco!")
        return -1



# 初始化一个串口, port为COM口号，baut为波特率
def init(port, baut):
    try:
        result = serial.Serial(port, baut)
        return result
    except:
        print("Error Port selected")
        return -1

def free(com):
    try:
        com.close()
        return 0
    except:
        print("Error Port selected")
        return -1

# 以字符形式发送命令
def send_cmd(dev, cmd): 
    print(cmd) # 打印日志 用于调试
    try:
        dev.isOpen()
        dev.write(bytes(cmd))# 将内容发送至串口
        return 0
    except:
        print("Com port is not open Yet!")
        return -1

# 用于实时手势识别使用的整体舵机运作命令
def full_motor_action(com, finger_index):
    finger = {} # 构建舵机:角度的字典
    cnt = 1 # 计数作为ID
    for i in finger_index:
        finger[cnt] = i
        cnt = cnt + 1
    send_cmd(com, protoco(ctx = finger)) 

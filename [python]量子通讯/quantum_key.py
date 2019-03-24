from quantum import Quantum
import random


class Observer:
    length = 20

    def __init__(self, name):
        self.name = name
        self.q_list = []  # 量子集合

    # 初始化量子集合
    def init_quantum(self):
        for i in range(Observer.length):
            self.q_list.append(Quantum())

    # 观测
    def observe(self):
        def __observe(quantum):
            ran = random.randint(0, 2)
            # 只使用a,b两个属性
            if (ran == 0):
                return ('a', q.get_a())
            else:
                return ('b', q.get_b())
        self.path = []
        self.result = []
        for q in self.q_list:
            result = __observe(q)
            self.path.append(result[0])
            self.result.append(result[1])
        print(self.name,'观测方式：', self.path)
        print(self.name,'观测结果：', self.result)
    
    # 从另一个观测者获取量子序列
    def get_quantum(self, another):
        self.q_list=another.q_list
    
    # 从另一个观测者获取观测方式
    def get_path(self, another):
        self.key = []
        for i in range(Observer.length):
            if (another.path[i] == self.path[i]):
                self.key.append(self.result[i])
        print(self.name,'秘钥：', self.key)

sender = Observer('发送者')
sender.init_quantum() # 初始化量子序列
sender.observe() # 对量子序列进行观测

reciver = Observer('接收者')
reciver.get_quantum(sender) # 发送者把量子传输给接收者
reciver.observe() # 接收者对其观测

# 双方交换观察方式
sender.get_path(reciver)
reciver.get_path(sender)

print('\n-----------模拟窃听-----------\n')

sender = Observer('发送者')
sender.init_quantum() # 初始化量子序列
sender.observe() # 对量子序列进行观测

interceptor = Observer('窃听者')
interceptor.get_quantum(sender) # 截取信息
interceptor.observe() # 观测

reciver = Observer('接收者')
reciver.get_quantum(interceptor) # 发送者把量子传输给接收者
reciver.observe() # 接收者对其观测

# 双方交换观察方式
sender.get_path(reciver)
reciver.get_path(sender)

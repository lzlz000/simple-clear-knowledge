import random

class Object:
    def __init__(self):
        self.__a = random.randint(0,1)
        self.__b = random.randint(0,1)
        self.__c = random.randint(0,1)
    
    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__b


class TreeNode:
        def __init__(self):
            self.__children = {}
            self.__val = random.randint(0,1)
        
        def set_child(self, name, child):
            self.__children[name]=child
            return child # 方便连续调用简化代码
        
        def get_child(self, name):
            return self.__children[name]
        
        def get_val(self):
            return self.__val

class Quantum:
    #关于叠加态 我们可以用树结构来维护
    #一个3个属性的量子，其叠加态总共有 3!=3*2*1=6 种状态，可表示为,
    #     root
    #   /   |   \
    #  a    b    c
    #  /\   /\   /\
    # b  c a  c a  b 
    # |  | |  | |  |
    # c  b c  a b  a
    

    # 测量方式，队列，如果新的测量属性和队列中最后一个值不一致则加入队列，
    # 如果队列长度大于（属性数-1）则头部数据出列，，为了便于理解，假设有abc三个属性
    # 测量属性 队列值
    # a       [a]
    # b       [a,b]  
    # c       [b,c]  
    # c       [b,c]   和最后一次测量一样 不发生改变
    # a       [c,a]  
    def __init__(self):
        self.route = []
        root = TreeNode()
        self.root = root
        root.set_child('a',TreeNode()).set_child('b',TreeNode()).set_child('c',TreeNode())
        root.get_child('a').set_child('c',TreeNode()).set_child('b',TreeNode())
        root.set_child('b',TreeNode()).set_child('a',TreeNode()).set_child('c',TreeNode())
        root.get_child('b').set_child('c',TreeNode()).set_child('a',TreeNode())
        root.set_child('c',TreeNode()).set_child('a',TreeNode()).set_child('b',TreeNode())
        root.get_child('c').set_child('b',TreeNode()).set_child('a',TreeNode())
    
    def __get(self, name):
        length = len(self.route)
        if (length == 0 or self.route[-1]!=name):
            self.route.append(name)
            if (len(self.route) >2):
                self.route.pop(0)
        node = self.root
        for name in self.route:
            node = node.get_child(name)
        return node.get_val()


    def get_a(self):
        return self.__get('a')

    def get_b(self):
        return self.__get('b')

    def get_c(self):
        return self.__get('c')


if __name__ == "__main__":
    o = Object()
    print("a:"+str(o.get_a())+" b:"+str(o.get_b())+" c:"+str(o.get_c()))
    print("b:"+str(o.get_b())+" a:"+str(o.get_a()))
    print("c:"+str(o.get_c())+" b:"+str(o.get_b()))
    print("a:"+str(o.get_a())+" c:"+str(o.get_c()))

    print('\n------------分割线-------------\n')
    q = Quantum()
    print('a',q.get_a())
    print('b',q.get_a())
    print('a',q.get_b())
    print('c',q.get_c())
    print('a',q.get_a())
    print('b',q.get_a())
    print('a',q.get_a())



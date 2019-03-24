# 欧几里得算法 （辗转相除法） 求最大公约数
def gcd(m, n):
    mod = 1
    # 将小数放到d1中
    if(m <= n):
        d1 = m
        d2 = n
    else:
        d1 = n
        d2 = m

    while mod != 0:
        mod = d2 % d1
        d2 = d1
        d1 = mod
    return d2


'''
找出质数 p q
n = p * q
φ(n) = (p-1)(q-1)  // 欧拉函数
公钥e: 1<e<φ(n)的整数 且和 φ(n)互质
私钥d: e*d%φ(n)==1

加密算法
m -> m^e%n 取得余数c
解密算法
c -> c^d%n 取得m
'''
# 真实情况下应该是很大的素数 通常为512、1024、2048位二进制数,如1024位二进制整数大约为十进制10^308数量级
# 计算得到秘钥然后以一定规则编码成字符串形式，形成常见的秘钥
p = 41
q = 43
n = p * q
# 欧拉函数
phi = (p-1)*(q-1)
# 1<e<φ(n)的整数 且和 φ(n)互质
publicKey = 2
# 此处相当于取得了一个满足上述条件的最大值
while gcd(phi, publicKey) != 1:
    publicKey = publicKey+1

# 私钥d: e*d%φ(n)==1
privateKey = (phi + 1) * publicKey
print("公钥:", publicKey,"私钥:", privateKey,"n:", n)
# 所有数据进行传递的时候都是序列化的，序列化后的任何信息可以认为是一串数字
content = 412  # 密文的值要小于 p * q
cipher = pow(content, publicKey, n)
print("密文", cipher)
content1 = pow(cipher, privateKey, n)
print("明文", content1)

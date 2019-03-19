package lzlz000.rsa;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

/**
 * 找出质数 p q
 * n = p * q
 * φ(n) = (p-1)(q-1)  // 欧拉函数
 * 公钥e: 1<e<φ(n)的整数 且和 φ(n)互质
 * 私钥d: e*d%φ(n)==1
 *
 * 加密算法
 * m -> m^e%n 取得余数c
 * 解密算法
 * c -> c^d%n 取得m
 *
 */
public class SimpleRSA {

    public static void main(String[] args){
        List<Integer> i = new ArrayList<Integer>();
        // 真实情况下应该是很大的素数 通常为1024位二进制数,大约为十进制10^308
        // 计算得到秘钥然后以一定规则编码成字符串形式，形成常见的秘钥
        // 因此，RSA的主要缺点之一就是受到素数产生技术的限制，运算代价高、速度慢，
        // 产生密钥困难，难以做到一次一密。快速产生大素数成为RSA算法的关键技术之一
        long p = 41;
        long q = 43;
        long n = p * q;
        // 欧拉函数
        long t = (p-1)*(q-1);
        // 1<e<φ(n)的整数 且和 φ(n)互质
        long publicKey = t - 1;
        // 此处相当于取得了一个满足上述条件的最大值
        // 获取公钥的时间复杂度是 NlogN
        while (euclid(t,publicKey)!=1){
            publicKey --;
        }
        // 私钥d: e*d%φ(n)==1
        long privateKey = (t + 1) * publicKey;
        System.out.println(publicKey+", "+privateKey+ ", "+t+ ", ");
        // 所有数据进行传递的时候都是序列化的，序列化后的任何信息可以认为是一串数字
        long content = 412; // 密文的值要小于 p * q
        long cipher = encrypt(content,publicKey,n);
        System.out.println("密文: "+cipher);
        System.out.println("明文: "+ decrypt(cipher,privateKey,n));
    }

    /**
     * 欧几里得算法 （辗转相除法） 求最大公约数
     * 欧几里得算法的时间复杂度是 logN 级别的
     */
    private static long euclid(long m, long n){
        long d1,d2;
        long mod = 1;
        //将小数放到d1中
        if(m<=n) {
            d1=m;
            d2=n;
        }else {
            d1=n;
            d2=m;
        }
        while(mod!=0) {
            mod= d2%d1;
            d2=d1;
            d1=mod;
        }
        return d2;
    }

    /**
     * 加密算法
     * 进行加密运算时，需要使用公钥和 两个质数乘积 n
     * 这两个值也是公开传播的
     * 加密算法
     * m -> m^e%n 取得余数c
     */
    private static long encrypt(long content, long publicKey, long n){
        BigInteger content1 = BigInteger.valueOf(content);
        BigInteger pow = content1.pow((int)publicKey);
        BigInteger mod = pow.mod(BigInteger.valueOf(n));
        return mod.longValue();
    }

    /**
     * 解密算法
     * c -> c^d%n 取得m
     *
     * 注意此处不可用 java.lang.Math.pow()取指数，数太大导致double取值是非精确的，取余数是错误的
     * 即使这样， BigInteger 仍然只能处理 本例子中这样很小的质数形成的秘钥 并且可以看到 解密过程有明显的 卡顿 效率不高
     * 因为 BigInteger求幂只能使用int 值，int值的上线作为私钥的上限（公钥显然小于私钥）显然是非常小、不安全的
     */
    private static long decrypt(long cipher, long privateKey, long n){
//        return (long)Math.pow(cipher,privateKey)%n; 错误
        BigInteger content1 = BigInteger.valueOf(cipher);
        BigInteger pow = content1.pow((int) privateKey);
        BigInteger mod = pow.mod(BigInteger.valueOf(n));
        return mod.longValue();
    }
}

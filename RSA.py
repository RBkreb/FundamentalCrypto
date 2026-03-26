from random import randrange
import math
_50primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
            37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
            79, 83, 89, 97, 101, 103, 107, 109, 113, 127,
            131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
            181, 191, 193, 197, 199, 211, 223, 227, 229, 233]
def odd(n):#生成大数
   if n<=1:
       return ValueError
   return randrange(2 ** (n - 1) + 1, 2 ** n, 2)
def getm(n):#伪素数选取
   while True:
       c = odd(n)
       for divisor in _50primes:
           if c % divisor == 0 and divisor ** 2 <= c:
               break
       return c
def mrcheck(n,k=20):#米勒拉宾素性检查
   if n<=3:
       return ValueError
   if n % 2 == 0:
       return False
   s, d = 0, n - 1
   while d % 2 == 0:
       d >>= 1
       s += 1
   for i in range(k):
       a = randrange(2, n - 1)
       x = pow(a, d, n)#费马小定理
       if x == 1 or x == n - 1:
           continue
       for p in range(s):
           x = pow(x, 2, n)#二次探测
           if x == n - 1:
               break
       else:
           return False
   return True
def getprime(bits):#大素数
   while True:
       pp = getm(bits)
       if mrcheck(pp):
           return pp
def ext_gcd(a, b):#扩展欧几里得
    if b == 0:
        return a, 1, 0
    else:
        r, x, y = ext_gcd(b, a % b)
        x,y = y,x - a // b * y
        return r, x, y
def key():#生成密钥对
    p=getprime(1024)
    q=getprime(1024)
    while p==q:
        q=getprime(1024)
    n=p*q
    e=65537
    fy=(p-1)*(q-1)
    x=ext_gcd(e,fy)[1]
    if x<0:
        x+=fy
    return (e,n),(x,n)
def multi(array,bin_array,n):#快速幂
    result=1
    for index in range(len(array)):
        a=array[index]
        if not int(bin_array[index]):
            continue
        result*=a
        result=result%n
    return result
def exp_mod(base,exp,n):#大数幂取模
    bin_array=bin(exp)[2:][::-1]
    r=len(bin_array)
    base_array=[]
    pre_base=base
    base_array.append(pre_base)
    for i in range(r-1):#确定幂乘底数序列
        next_base=(pre_base*pre_base)%n
        base_array.append(next_base)
        pre_base=next_base
    awb=multi(base_array,bin_array,n)
    return awb%n
def En(plain):#加密 
    cypher=[]
    for i in plain:
        cypher.append(exp_mod(ord(i),Pk[0],Pk[1]))
    return cypher
def De(cypher):#解密
    plain=[]
    for i in cypher:
        plain.append(exp_mod(i,Sk[0],Sk[1]))
    return plain
Pk,Sk=key()
print(Pk,'\n',Sk)
text="Hi,this is RSA!"
cypher=En(text)
for i in cypher:
    print(hex(i))
plain=De(cypher)
for i in plain:
    print(chr(i),end='')
import base64
S=list(range(256))
def generate(cypher,key,mode):
    if mode==2:
        cypher=base64.b64decode(cypher)
        cypher=bytes.decode(cypher)

    keysize=len(key)
    k=0
    for i in range(256):
        k=(k+S[i]+ord(key[i%keysize]))%256
        S[i],S[k]=S[k],S[i]
   
    i=k=0
    plain=[]
    for x in range(len(cypher)):
        i=(i+1)%256
        k=(k+S[i])%256
        S[k],S[i]=S[i],S[k]
        plain.append(chr(ord(cypher[x])^S[(S[i]+S[k])%256]))
    if mode==1:
        plain=str(base64.b64encode("".join(plain).encode("utf-8")),"utf-8")
        return plain
    else:
        return "".join(plain)

choice=int(input("选择加解密(加密1,解密2,退出其他):"))
while choice==1 or choice==2:
    key=input("密钥：")
    if choice==1:
        plain=input("明文：")
        cypher=generate(plain,key,1)
        print(cypher)
    elif choice==2:
        cypher=input("密文：")
        plain=generate(cypher,key,2)
        print(plain)
    S=list(range(256))
    choice=int(input("选择加解密(加密1,解密2,退出其他):"))
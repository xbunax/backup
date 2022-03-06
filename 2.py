n=input("请输入一个整数")
n=int(n)
if n>0 and n%2==0:
    print(n,"即是正数也是偶数")
elif n==0:
    print(n,"既不是正数也不是负数")
elif n>0 and n%2!=0:
    print(n,"是奇数、正数")
elif n<0 and n%2==0:
    print(n,"是负数、偶数")
elif n<0 and n%2!=0:
    print(n,"是奇数、负数")
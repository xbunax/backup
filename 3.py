n=input()
n=list(n.split("-"))
a=int(n[0])
b=int(n[1])
c=int(n[2])
d=[1,3,5,7,8,10,12]
e=[2,4,6,9,11]
if a%4==0 and a%100!=0 or a%400==0:
     if b>2 and b in d:
         m=d.index(b)

         print('第',m*31+(b-m-2)*30+29+c,'天')
     elif b>2 and b in e:
        t=e.index(b)
        print('第',(t-1)*30+(b-t-1)*31+29+c,'天')
else:
    if b > 2 and b in d:
        m = d.index(b)

        print('第', m * 31 + (b - m - 2) * 30 + 28 + c, '天')
    elif b > 2 and b in e:
        t = e.index(b)
        print('第', (t - 1) * 30 + (b - t - 1) * 31 + 28 + c, '天')


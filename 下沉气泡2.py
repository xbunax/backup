import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math as m
x=0.015370735#开始下沉位置距水面高度距离
rou=10.0**3#水的密度
g=10.0#重力加速度
H0=0.128331578#水的高度
f=150.0#频率
pe=10.0**5#大气压强
A=0.0127832#振幅
R=0.000999615#气泡半径
w=2*m.pi*f#角速度
vp=rou*H0*g/pe#无量纲参量
wp=A*w**2/g#无量纲参量
d=x/H0#高度比
b=A/R#振幅与半径比值
if vp*wp**2*d*0.5*(1-0.667*1.68*b**2/(2*(1+(1+1.68*b**2)**0.5)+1.68*b**2))>1:
    print('符合')
else:
    print('不符合')
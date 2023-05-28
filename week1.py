import numpy as np
import matplotlib.pyplot as plt
import random

def normal():
    k=np.random.default_rng().normal(2,1,1)[0]
    return k

def poisson():
    k=np.random.default_rng().poisson(2,1)[0]
    return k

def coin_toss():
    k=np.random.randint(0,2)
    if k==1:
        return 5
    else:
        return -6

def exponential():
    k=np.random.default_rng().exponential(3,1)[0]
    return k

def crazy_button():
    k=np.random.randint(0,4)
    if k==0:
        k=normal()
    elif k==1:
        k=poisson()
    elif k==2:
        k=coin_toss()
    else:
        k=exponential()
    return k

def reward(e):
    reward1=0
    reward2=0
    reward3=0
    reward4=0
    reward5=0

    freq1=0
    freq2=0
    freq3=0
    freq4=0
    freq5=0

    value1=0
    value2=0
    value3=0
    value4=0
    value5=0

    reward=[0]*1000

    for i in range(1000):
        if e==0:
                j=1
        else:
                j=np.random.randint(0,1/e)
        if i==1 or j==0:
            a=np.random.randint(0,5)
            if a==0:
                reward[i]=normal()
                reward1+=reward[i]
                freq1+=1
                value1=reward1/freq1
            elif a==1:
                reward[i]=poisson()
                reward1+=reward[i]
                freq2+=1
                value2=reward2/freq2
            elif a==2:
                reward[i]=coin_toss()
                reward3+=reward[i]
                freq3+=1
                value3=reward3/freq3
            elif a==3:
                reward[i]=exponential()
                reward4+=reward[i]
                freq4+=1
                value4=reward4/freq4
            elif a==4:
                reward[i]=crazy_button()
                reward5+=reward[i]
                freq5+=1
                value5=reward5/freq5
        else:
            g=max(value1,value2,value3,value4,value5)
            if g==value1:
                reward[i]=normal()
                freq1+=1
                value1=reward1/freq1
            elif g==value2:
                reward[i]=poisson()
                reward1+=reward[i]
                freq2+=1
                value2=reward2/freq2
            elif g==value3:
                reward[i]=coin_toss()
                reward3+=reward[i]
                freq3+=1
                value3=reward3/freq3
            elif g==value4:
                reward[i]=exponential()
                reward4+=reward[i]
                freq4+=1
                value4=reward4/freq4
            elif g==value5:
                reward[i]=crazy_button()
                reward5+=reward[i]
                freq5+=1
                value5=reward5/freq5
    return reward

def average(p):
    mean=[0]*1000
    for i in range(1000):
        u=reward(p)
        for j in range(1000):
            mean[j]+=u[j]/1000
    return mean

x=[i+1 for i in range(1000)]

plt.plot(x,average(0),label="e=0")
plt.plot(x,average(0.01),label="e=0.01")
plt.plot(x,average(0.1),label="e=0.1")
plt.plot(x,average(0.2),label="e=0.2")
plt.plot(x,average(0.3),label="e=0.3")

plt.legend()
plt.show()







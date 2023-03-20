import matplotlib.pyplot as plt
import numpy as np
import math
from pylab import *
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
def weightFunction(u):
    fig = plt.figure(figsize=(12,8), dpi=72)
    x = np.arange(0.0001 , 1.0001 , 0.0001)
    plt.xlabel('p')
    plt.ylabel('w(p)')
    plt.title('weight function')
    for i in u:
        y = [math.exp( - ( - math.log (a) ) ** i ) for a in x]  
        plt.plot(x,y,label='u='+str(i))
    plt.legend(loc='upper left')
    xlim(0,1)
    ylim(0,1)
    plt.show()
    
def s_shape_function(x,lamda,beta,gamma):
    if x<0 :
        return (-1 * lamda) * ((-1 * x ) ** gamma)
    elif x==0 :
        return 0.0
    else:
        return x ** beta
    
    
def value_function(set_lamda_beta_gamma):
    fig = plt.figure(figsize=(12,8), dpi=72)
    x = np.arange(-2 , 2 , 0.001)
    plt.xlabel('x')
    plt.ylabel('v(x)')
    plt.title('value function')
    for i in set_lamda_beta_gamma:
        y = np.array([s_shape_function(a,i[0],i[1],i[2]) for a in x])
        plt.plot(x,y,label='lambda='+str(i[0])+' beta='+str(i[1])+' gamma='+str(i[2]))
    plt.legend(loc='upper left')
    xlim(-2,2)
    ylim(-3,2)
    plt.show()
    
value_function([(1.,0.3,0.3),(1.,1.,1.),(2.,0.3,0.6),(2.,0.6,0.6)])    
    
    
    
#weightFunction([0.4,0.6,0.8,1.])

#github

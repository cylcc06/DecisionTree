import matplotlib as mpl
#mpl.use('Agg')
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,axis,show
from pylab import *
from matplotlib.ticker import MultipleLocator

from matplotlib.ticker import FormatStrFormatter

def showlogist(u,r):

    # ---------------------------------------------------
    # 将x主刻度标签设置为20的倍数(也即以 20为主刻度单位其余可类推)
    xmajorLocator = MultipleLocator(1);

    # 设置x轴标签文本的格式
    xmajorFormatter = FormatStrFormatter('%1.1f')

    # 将x轴次刻度标签设置为5的倍数
    xminorLocator = MultipleLocator(0.1)
    # 设定y 轴的主刻度间隔及相应的刻度间隔显示格式
    #       将y轴主刻度标签设置为1.0的倍数
    ymajorLocator = MultipleLocator(0.1)
    # 设置y轴标签文本的格式
    ymajorFormatter = FormatStrFormatter('%1.1f')
    # 将此y轴次刻度标签设置为0.2的倍数
    yminorLocator = MultipleLocator(0.05)
    xlist=np.arange(-1+u,1+u,0.001)
    ylist=[]
    for x in xlist:
       ylist.append(1/(1+np.exp(-(x-u)/r)))
    axis([-1+u,1+u,0,1])
    plt.figure(1)

    # 注意:一般都在ax中设置,不再plot中设置
    ax = subplot(111)
    plot(xlist,ylist)

    # 设置主刻度标签的位置,标签文本的格式
    ax.xaxis.set_major_locator(xmajorLocator)
    ax.xaxis.set_major_formatter(xmajorFormatter)

    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_major_formatter(ymajorFormatter)

    # 显示次刻度标签的位置,没有标签文本
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)

    ax.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
    ax.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度

    plt.show()

if __name__ =='__main__':
    showlogist(10,0.02)
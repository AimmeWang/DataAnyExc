
"""
描述： 王婷同学的学习资料
时间：2018-12-7
作者：Acmen
"""

import numpy as np
import matplotlib.pyplot as plt

"""
回顾新东西：
1. matplotlib: 画图的一个库
2. numpy: 数组的封装库
3. 从互联网上获取别人写好的开源库：pip install xxxxx 写入到一个后缀为bat文件中
4. 利用numpy和matplotlib画了一张图
"""
def PlotShow():
	x = np.array([1,2,3,4,5,6,7,8])
	y = np.array([3,5,7,6,2,6,10,15])
	plt.plot(x, y, 'r')
	plt.bar(x, y, 0.2, alpha=1, color='b')
	plt.show()

PlotShow()


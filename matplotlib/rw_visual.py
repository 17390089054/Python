import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw=RandomWalk()
    rw.fill_walk()
    #设置绘图窗口的尺寸
    plt.figure(dpi=141,figsize=(10,6))
    
    point_numbers=list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
                edgecolor='none',cmap=plt.cm.Blues,s=15)
    
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
                edgecolors='none',s=100)
    
    plt.show()

    keep_running=input("Make another walk?(y/n):")
    if keep_running=='n':
        break
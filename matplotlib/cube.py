import matplotlib.pyplot as plt

x_values=range(1,5001)
y_values=[y**3 for y in x_values]
plt.scatter(x_values,y_values,edgecolor='none',
            cmap=plt.cm.Reds,c=y_values,s=10)
#设置图表的标题并给坐标轴加上标签
plt.title("Cube of numbers ",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cube of Value",fontsize=14)


plt.plot(x_values,y_values,linewidth=2)
#保存图片
#plt.savefig("cube2.png",bbox_inches='tight')
plt.show()

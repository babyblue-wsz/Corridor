import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from Calculate import cal_slope

if __name__ == '__main__':
    f = open('../static/Anhui.txt', 'r', encoding='utf-8')

    lines = f.readlines()
    print('Total amount: %s' % len(lines))

    x_list = []
    y_list = []
    data_list = []

    # todo 创建大矩阵matrix，设初始值-100，将真实数据点覆盖进去。结果是大面积空值，浪费性能
    matrix = np.full((900, 3500), -100, dtype=np.int16)
    print(type(matrix))

    # todo 读取原xyz文件，获取初始坐标点集合（坐标原点归零处理后的）。原数据 x_min = 489591，y_min = 3490656
    for line in lines:
        temp = line.split('\t')

        x = int(float(temp[0])) - 489591
        y = int(float(temp[1])) - 3490656
        z = float(temp[2].strip())

        x_list.append(x)
        y_list.append(y)
        # data_list.append([x, y, z])

        if 2750 <= x <= 3650 and 53000 <= y <= 56500:
            matrix[x-2751][y - 53001] = z

    f.close()
    # np.savetxt('./data.txt', matrix, fmt='%d')

    # todo  画坡度图
    slope = cal_slope(matrix)
    im2 = plt.matshow(slope, norm=matplotlib.colors.Normalize(vmin=0, vmax=8, clip=False))  # 画彩色图
    # im2 = plt.matshow(slope, cmap=plt.cm.gray)  # 画灰度图

    cb2 = plt.colorbar(im2)
    # 更改坐标轴位置和刻度，方便后面划分网格
    # ax = plt.gca()
    # ax.set_xticks(np.arange(-0.5, len(matrix[0]), 1))
    # ax.set_yticks(np.arange(-0.5, len(matrix), 1))
    # ax.set_xticklabels(np.arange(0, len(matrix[0]) + 1, 1))
    # ax.set_yticklabels(np.arange(0, len(matrix) + 1, 1))

    # ax.grid(color='black', linestyle='-', linewidth=1)
    plt.show()

    # todo 画x y散点图
    # 定义颜色变量
    # color = ['c', 'b', 'g', 'r', 'm', 'y', 'k', 'w']
    # plt.scatter(x_list, y_list, c=color[1], edgecolors='r')
    # plt.show()

    # todo 将坐标点集合保存至coords.txt文件
    # f = open('./coords.txt', 'w')
    # f.write(str(data_list))
    # f.close()

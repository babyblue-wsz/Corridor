import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from Slop.Calculate import cal_slope
from APlus.test import *
from DFS import SearchPath2

if __name__ == '__main__':
    f = open('static/XYZ-100m.txt', 'r', encoding='utf-8')

    lines = f.readlines()
    print('Total amount: %s' % len(lines))

    x_list = []
    y_list = []
    z_list = []
    trash_list = []
    data_list = []

    # todo 创建大矩阵matrix，设初始值-100，将真实数据点覆盖进去。结果是大面积空值，浪费性能
    matrix = np.full((150, 420), 200, dtype=np.int16)

    # todo 读取原xyz文件，获取初始坐标点集合（坐标原点归零处理后的）。原数据 x_min = 489591，y_min = 3490656
    for line in lines:
        temp = line.split(',')

        x = int(float(temp[0]) / 100) - 4900
        y = int(float(temp[1]) / 100) - 34980
        if temp[2].strip() == '-1e+09':
            # trash_list.append(temp[2].strip())
            z = 200
        else:
            z = int(float(temp[2].strip()))

        # x_min 490264
        # x_max 504464
        # y_min 3498761
        # y_max 3537861

        x_list.append(x)
        y_list.append(y)
        # data_list.append([x, y, z])

        matrix[x][y] = z

    print(min(x_list))
    print(max(x_list))
    print(min(y_list))
    print(max(y_list))
    f.close()
    slope = cal_slope(matrix, 100)
    # np.savetxt('./data.txt', matrix, fmt='%d')

    # todo  画坡度图
    # im2 = plt.matshow(slope, norm=matplotlib.colors.Normalize(vmin=0, vmax=20, clip=False))  # 画彩色图
    # cb2 = plt.colorbar(im2)
    # plt.show()

    # 算路径
    total_results = []
    start_position1 = Position(11, 380)
    target_position1 = Position(37, 262)
    res1 = SearchPath(slope, start_position1, target_position1)
    if res1:
        for temp in res1:
            total_results.append([(temp[0] + 4900) * 100, (temp[1] + 34980) * 100])
            slope[temp[0], temp[1]] = 15

    start_position2 = Position(37, 256)
    target_position2 = Position(48, 145)
    res2 = SearchPath(slope, start_position2, target_position2)
    if res2:
        for temp in res2:
            total_results.append([(temp[0] + 4900) * 100, (temp[1] + 34980) * 100])
            slope[temp[0], temp[1]] = 15

    start_position3 = Position(57, 130)
    target_position3 = Position(136, 15)
    res3 = SearchPath(slope, start_position3, target_position3)
    if res3:
        for temp in res3:
            total_results.append([(temp[0] + 4900) * 100, (temp[1] + 34980) * 100])
            slope[temp[0], temp[1]] = 15

    im2 = plt.matshow(slope, norm=matplotlib.colors.Normalize(vmin=0, vmax=20, clip=False))  # 画彩色图
    # im2 = plt.matshow(slope, cmap=plt.cm.gray)  # 画灰度图

    cb2 = plt.colorbar(im2)
    # 更改坐标轴位置和刻度，方便后面划分网格
    # ax = plt.gca()
    # ax.set_xticks(np.arange(-0.5, len(slope[0]), 1))
    # ax.set_yticks(np.arange(-0.5, len(slope), 1))
    # ax.set_xticklabels(np.arange(0, len(slope[0]) + 1, 1))
    # ax.set_yticklabels(np.arange(0, len(slope) + 1, 1))
    plt.show()

    # todo  保存路径点坐标
    # note = open('corridor-100m.txt', mode='w', encoding='utf-8')
    # for each_res in total_results:
    #     note.write(str(each_res[0]) + ' ' + str(each_res[1]) + '\n')
    # note.close()

    # todo  画matrix原图
    # im2 = plt.matshow(matrix, norm=matplotlib.colors.Normalize(vmin=10, vmax=200, clip=False))  # 画彩色图
    # cb2 = plt.colorbar(im2)
    # ax = plt.gca()
    # ax.invert_yaxis()
    # plt.show()

    # todo 画x y散点图
    # 定义颜色变量
    # color = ['c', 'b', 'g', 'r', 'm', 'y', 'k', 'w']
    # plt.scatter(x_list, y_list, c=color[1], edgecolors='r')
    # plt.show()

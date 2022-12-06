import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
from Slop.Calculate import cal_slope

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
    # matrix = np.full((400, 150), 200, dtype=np.int16)
    matrix = np.full((150, 420), 200, dtype=np.int16)

    # todo 读取原xyz文件，获取初始坐标点集合（坐标原点归零处理后的）。原数据 x_min = 489591，y_min = 3490656
    for line in lines:
        temp = line.split(',')

        x = int(float(temp[0]) / 100) - 4900
        y = int(float(temp[1]) / 100) - 34980

        # x = int((float(temp[0]) - 490264) / 100)
        # y = int((float(temp[1]) - 3498761) / 100)
        if temp[2].strip() == '-1e+09':
            # continue
            z = 200
            # trash_list.append(temp[2].strip())
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

    f.close()



    im2 = plt.matshow(matrix)  # 画彩色图
    cb2 = plt.colorbar(im2)
    ax = plt.gca()
    ax.invert_yaxis()
    plt.show()





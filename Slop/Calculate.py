import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange
import seaborn as sns
import matplotlib.colors


def cal_gradient_horizon(nums, x, y, x_cellsize):
    ans = (nums[x - 1][y + 1] + 2 * nums[x][y + 1] + nums[x + 1][y + 1] -
           (nums[x - 1][y - 1] + 2 * nums[x][y - 1] + nums[x + 1][y - 1])) \
          / (8 * x_cellsize)
    return ans


def cal_gradient_vertical(nums, x, y, y_cellsize):
    ans = (nums[x + 1][y - 1] + 2 * nums[x + 1][y] + nums[x + 1][y + 1] -
           (nums[x - 1][y - 1] + 2 * nums[x - 1][y] + nums[x - 1][y + 1])) \
          / (8 * y_cellsize)
    return ans


def cal_single_point_slope(nums, height, width, x, y, x_cellsize, y_cellsize):
    if x == 0 or x == height - 1 or y == 0 or y == width - 1:
        return 0.0
    dzdx = cal_gradient_horizon(nums, x, y, x_cellsize)
    dzdy = cal_gradient_vertical(nums, x, y, y_cellsize)
    ans = math.atan(math.sqrt(dzdx ** 2 + dzdy ** 2)) * 57.29578
    return ans


def cal_slope(nums):
    m = len(nums)
    n = len(nums[0])
    slope = np.zeros((m, n), dtype=float)
    for i in range(m):
        for j in range(n):
            slope[i][j] = cal_single_point_slope(nums, m, n, i, j, 5, 5)
    return slope


if __name__ == '__main__':
    # nums = np.array([[50, 45, 50],
    #                  [30, 30, 30],
    #                  [8, 10, 10]])
    nums = np.random.random((20, 20))
    slope = cal_slope(nums)
    # sns.heatmap(slope, linewidths=0.02, vmax=100, vmin=0, cmap='rainbow')

    im2 = plt.matshow(slope, norm=matplotlib.colors.Normalize(vmin=0, vmax=1, clip=False))
    cb2 = plt.colorbar(im2)
    # 更改坐标轴位置和刻度，方便后面划分网格
    ax = plt.gca()
    ax.set_xticks(np.arange(-0.5, len(nums[0]), 1))
    ax.set_yticks(np.arange(-0.5, len(nums), 1))
    ax.set_xticklabels(np.arange(0, len(nums[0]) + 1, 1))
    ax.set_yticklabels(np.arange(0, len(nums) + 1, 1))
    ax.grid(color='black', linestyle='-', linewidth=1)

    plt.show()

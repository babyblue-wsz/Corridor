def IsInBoard(mapp, i, j):
    if 0 <= i < len(mapp) and 0 <= j < len(mapp[i]) and mapp[i][j] < 20:
        return 1
    else:
        return 0


def SearchPath2(matrix, start, end, results):
    return dfs(matrix, start, end, results)


def dfs(matrix, current, end, results):
    current_x = current[1]
    current_y = current[0]
    results.append([current_x, current_y])
    if current == end:
        print("成功找到解")
        return results
    if IsInBoard(matrix, current_y, current_x):
        max = -10.0
        temp_pos = []
        if matrix[current_y - 1, current_x] >= max:
            temp_pos = [current_y - 1, current_x]
        if matrix[current_y - 1, current_x - 1] >= max:
            temp_pos = [current_y - 1, current_x - 1]
        if matrix[current_y, current_x - 1] >= max:
            temp_pos = [current_y, current_x - 1]
        if matrix[current_y + 1, current_x - 1] >= max:
            temp_pos = [current_y + 1, current_x - 1]
        if matrix[current_y + 1, current_x] >= max:
            temp_pos = [current_y + 1, current_x]
        print(temp_pos[0], temp_pos[1])
        dfs(matrix, [temp_pos[0], temp_pos[1]], end, results)

# from collections import defaultdict
#
#
# def shortestDistance(maze, start, destination):
#     m, n = len(maze), len(maze[0])
#     direcs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
#     start, destination = tuple(start), tuple(destination)
#     # 下面广度优先遍历
#     que = [[start, 0]]
#     visited = defaultdict(int)
#     visited[start] = 0
#     # 因为广度优先遍历第一次找到的不一定是最短距离 所以保存一下 res=steps
#     res = float('inf')
#     while que:
#         pos, steps = que.pop(0)
#         # print('pos={} steps={}'.format(pos, steps))
#         for direc in direcs:
#             nex_pos, add_steps = roll(pos, direc, maze)
#             nex_steps = steps + add_steps
#             if nex_pos == destination:
#                 res = min(res, nex_steps)
#             if nex_pos not in visited or nex_steps < visited[nex_pos]:
#                 que.append([nex_pos, nex_steps])
#                 visited[nex_pos] = nex_steps
#         print('que={}'.format(que))
#     # return res if res != float('inf') else -1
#
#
# # 表示从pos=(x,y) 沿着(dx, dy)方向 到达的位置 用的步数
# def roll(pos, direc, maze):
#     m, n = len(maze), len(maze[0])
#     x, y = pos
#     dx, dy = direc
#     steps = 0
#     # 只要不出界and不碰到墙 就严格一个方向滚
#     while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
#         # print('maze[{}][{}]={}'.format(x,y,maze[x][y]))
#         x, y = x + dx, y + dy
#         steps += 1
#     # 如果出界导致循环停止 最后停在墙上 因此后退一步
#     x, y = x - dx, y - dy
#     return (x, y), steps - 1

# # with open("hello.txt", mode="r", encoding="utf-8") as file:
# #     for index, line in enumerate(file.readlines()):
# #         print(f"line {index + 1}: {line}")
#
# print(ord("1"))
# print(ord("a"))
#
# # box_list = ["ykc 82 01", "eo first qpx", "eo first qpx", "09z cat hamster", "06f 12 25 6", "az0 first qpx",
# #             "236 cat dog rabbit snake"]
# #
# #
# # def sort_boxes(box_list: list[str]) -> list[str]:
# #     unsorted = [x for x in box_list if x.split()[1].isdigit()]
# #     to_be_sorted = sorted([x for x in box_list if not x.split()[1].isdigit()])
# #
# #     return [" ".join(x) for x in sorted([box.split() for box in to_be_sorted],
# #                                         key=lambda x: x[1:])] + unsorted
# #
# #
# # print(sort_boxes(box_list))
# #
# # def get_items(entries):
# #     import heapq
# #
# #     priority_queue = []
# #     result = []
# #     next_item = 1
# #     for entry in entries:
# #         if entry[0] == "INSERT":
# #             heapq.heappush(priority_queue, entry)
# #         if entry[0] == "VIEW":
# #             result.append(heapq.nsmallest(next_item, priority_queue, key=lambda x: int(x[2]))[-1])
# #             next_item += 1
# #
# #     return result
#
# import itertools
#
# needed = 10000
# f = [[1, 3000], [2, 5000], [3, 7000], [4, 10000]]
# r = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
# map_ = {}
# for idx, anything in enumerate(itertools.product(f, r)):
#
#     length = max(len(f), len(r))
#     row = idx // length + 1
#     col = idx % length + 1
#     what = anything[0][1] + anything[1][1]
#     if what <= needed:
#         map_[(row, col)] = what
#
# if len(map_) < 1:
#     pass
# print(map_)
# max_needed = max(map_.values())
#
# print([list(key) for key, value in map_.items() if value == max_needed])


# print(f"{idx // length} {idx % length} --> {anything}")
#
#
# def longest_even_length(sentence: str) -> str:
#     return max((word for word in sentence.split() if len(word) % 2 == 0), key=len)
#
#
# print(longest_even_length("Time to write great code"))
#
#
# class Presentation:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __lt__(self, other):
#         return self.end < other.end
#
#
# def max_presentations(scheduleStart, scheduleEnd):
#     from bisect import bisect
#     presentations = sorted([Presentation(i, j) for i, j in zip(scheduleStart, scheduleEnd)])
#
#     result = []
#
#     for presentation in presentations:
#         i = bisect(result, presentation.start)
#
#         if i == len(result):
#             result.append(presentation.end)
#         elif presentation.end < result[i]:
#             result[i] = presentation.end
#     return len(result)
#
#
# print(max_presentations([1, 1, 2], [3, 2, 4]))
#
#
# def findSongs(rideDuration, songDurations):
#     lst = []
#     for i in range(len(songDurations)):
#         for j in range(len(songDurations)):
#             if i != j and songDurations[i] + songDurations[j] <= rideDuration - 30:
#                 lst.append([i, j, songDurations[i], songDurations[j], songDurations[i] + songDurations[j]])
#
#     return max(lst, key=lambda x: x[4])[:2]
#
#
# # def minimum_distance(area: list[list]) -> int:
# #     from collections import deque
# #     if area is None or not area:
# #         return -1
# #
# #     visited = set()
# #     queue = deque()
# #
# #     queue.append([0, 0])
# #     visited.add("0,0")
# #
# #     distance = 0
# #
# #     moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# #
# #     while len(queue) != 0:
# #         size = len(queue)
# #         for i in range(size):
# #             point = queue.pop()
# #
# #             if area[point[0]][point[1]] == 0:
# #                 return distance
# #
# #             for move in moves:
# #                 x = point[0] + move[0]
# #                 y = point[1] + move[1]
# #
# #                 if x >= 0 and x < len(area) and y >= 0 and y < len(area[0]) and area[x][y] != 0 and f"{x},{y}" not in visited:
# #                     queue.append([x, y])
# #                     visited.add(f"{x},{y}")
# #         distance += 1
# #
# #     return -1
# #
# # print(minimum_distance([[1, 0, 0], [1, 0, 0], [1, 9, 1]]))
#
# def dnacomplement(s):
#     complements = dict(zip("ATCG", "TAGC"))
#     print(complements)
#
#     return "".join(complements[key] for key in reversed(s))
#
#
# print(dnacomplement("GATC"))
#
#
# def solve(X, arr, query_value):
#     if arr.count(X) == 0:
#         return -1
#
#     lst = []
#     pos = -1
#     for i in range(arr.count(X)):
#         try:
#             pos = arr.index(X, pos+1)
#             lst.append(pos)
#         except ValueError:
#             break
#
#     print("LST",lst)
#     return [lst[value - 1] + 1 if value <= arr.count(X) else -1 for value in query_value]
#
#
# # print(solve(8, [1, 2, 20, 8, 8, 1, 2, 5, 8, 0], [100, 2, 1, 3, 4]))
# print(solve(9, [9,8,9,9], [7,3,7,6]))
#
#
# def min_num(sam_daily, kelly_daily, difference):
#     if sam_daily >= kelly_daily:
#         return -1
#
#     new_sam_daily = sam_daily + difference
#     new_kelly_daily = kelly_daily
#     no_of_days = 1
#     while new_sam_daily >= new_kelly_daily:
#         new_sam_daily += sam_daily
#         new_kelly_daily += kelly_daily
#         no_of_days += 1
#
#     return no_of_days
#
# # print(minNum(3, 5, 5)) #3
# # print(minNum(4, 5, 1)) #2
#

# import itertools
# import heapq
# res = []
# stuff = [1, 2, 3]
# for L in range(0, len(stuff)+1):
#     for subset in itertools.combinations(stuff, L):
#         heapq.heappush(res, sum(subset))

# print(heapq.nlargest(3, (sum(subset) for L in range(0, len(stuff) + 1) for subset in itertools.combinations(stuff, L))))
# print(heapq.nlargest(3, res))

# def count_max(upright):
#     from itertools import product
#     every = [k.split() for k in upright]
#     row_max = max(int(i[0]) for i in every)
#     col_max = max(int(i[1]) for i in every)
#
#     # grids = {
#     #     (1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0,
#     #     (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0,
#     #     (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0,
#     #     (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0,
#     #
#     # }
#     grids = {}
#
#     for i, j in product(range(1, row_max+1), range(1, col_max+1)):
#         grids[(i, j)] = 0
#
#     print(grids)
#     for up in upright:
#         i, j = [int(k) for k in up.split()]
#         for grid in grids.keys():
#
#             if grid[0] <= i and grid[1] <= j:
#                 print("Adding", i, j)
#                 grids[(i, j)] += 1
#
#
#     max_num = max(grids.values())
#     print(grids)
#     return len([selected for selected in grids.values() if selected == max_num])
#
# print(count_max(["1 4", "2 3", "4 1"]))
# print(count_max(["2 3", "3 7", "4 1"]))

# def get_one_bits(n):
#     bits = bin(n)[2:]
#     return [bits.count('1')] + [index for index, element in enumerate(bits, start=1) if element == '1']
#
#
# print(get_one_bits(161))

import math


# mat = [[2, 5, 6], [16, 17, 12], [3, 10, 18]]
# count = 0
#
# for i, m in enumerate(mat):
#     if math.gcd(*m) != 1:
#         count += 1
#         m[i] = 1
#
# print(count)

def solve(n, m, mat):
    import math

    count = 0
    for i, m in enumerate(mat):
        if math.gcd(*m) != 1:
            count += 1
            m[i] = 1
    return count


# 2 4 10 20000 7 14 3 20

def setBitCounts(L, K):
    R = L
    bits = bin(L).count('1')
    while bits < K:
        R += 1
        bits += bin(R).count('1')

    return R


"""
https://leetcode.com/problems/k-closest-points-to-origin/
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
 return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
 (except for the order that it is in).
"""
import math
import heapq


def closest_k_points(points, k):
    """
    Appends the distance as the third element to each point
    Sort points based on the third value
    Return the k points in the expected format

    :param points:
    :param k:
    :return:
    """
    for point in points:
        point.append(math.sqrt(((0 - point[0]) ** 2) + ((0 - point[1]) ** 2)))
    points.sort(key=lambda k: k[2])
    return [point[:2] for point in points]


def closest_k_heap(points, k):
    heap = []
    for point in points:
        dist = [math.sqrt(((0 - point[0]) ** 2) + ((0 - point[1]) ** 2))*-1] + point
        if len(heap) == k:
            heapq.heappushpop(heap, dist)
        else:
            heapq.heappush(heap, dist)

    return [i[1:] for i in heap]


points = [[1, 3], [-2, 2]]
k = 1
# print(closest_k_points(points, k))
print(closest_k_heap(points, k))

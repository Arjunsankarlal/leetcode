"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n):
    """
    This method uses recursion, but it will take exponential time, which will fail at mere n value of 45

    :param n:
    :return:
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    return climb_stairs(n - 1) + climb_stairs(n - 2)


def climb_stairs_bottom_up(n):
    """
    This dynamic programming approach is a bottom up approach where we calculate data based on the previous data

    :param n:
    :return:
    """
    mapping = dict()
    mapping[0] = 0
    mapping[1] = 1
    mapping[2] = 2
    mapping[3] = 3
    if n <= 3:
        return mapping[n]
    for i in range(4, n + 1):
        mapping[i] = mapping[i - 1] + mapping[i - 2]
    return mapping[n]


print(climb_stairs_bottom_up(45))

import bisect
from math import sqrt

from map.Axis import Axis


def find_le(a, x):
    i = bisect.bisect_right(a, x)
    if i:
        return i - 1
    return -1


def find_ge(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i
    return -1


class BinarySearchMatrix:
    def __init__(self, dimensions=2):
        self.dimensions = dimensions
        self.main_axis = []

    def add(self, vector: [], data):
        axis = self.main_axis
        next_axis = None
        for value in vector:
            if len(axis) == 0:
                next_axis = Axis(value)
                axis.insert(0, next_axis)
            else:
                axis_index = find_le(axis, value)
                if axis_index > -1 and float(axis[axis_index]) == value:
                    next_axis = axis[axis_index]
                else:
                    next_axis = Axis(value)
                    axis.insert(axis_index + 1, next_axis)
            axis = next_axis.contained_values
        if next_axis is not None:
            next_axis.data = data

    def radial_knn(self, point, radio):
        top_limits = []
        lower_limits = []
        for value in point:
            top_limits.append(value + radio)
            lower_limits.append(value - radio)
        axis = Axis(0)
        axis.contained_values = self.main_axis
        return self.recursion(axis, lower_limits, top_limits, point, 0, radio ** 2)

    def recursion(self, axis, lower_limits: [], top_limits: [], point: [], cumulative_radius=0, square_radius=0,
                  dimension=0):
        if dimension == self.dimensions:
            return [axis.data]
        if cumulative_radius > square_radius:
            return []
        if dimension == self.dimensions - 1:
            radius_excess = sqrt(square_radius - cumulative_radius)
            l_limit = point[dimension] - radius_excess
            t_limit = point[dimension] + radius_excess
        else:
            l_limit = lower_limits[dimension]
            t_limit = top_limits[dimension]

        axis = axis.contained_values
        t_index = find_le(axis, t_limit)
        l_index = find_ge(axis, l_limit)
        if t_index == -1 or l_index == -1:
            return []
        items = []
        for next_dimension in range(l_index, t_index + 1):
            next_cumulative_radius = cumulative_radius + (float(axis[next_dimension]) - point[dimension]) ** 2
            items = items + self.recursion(axis[next_dimension], lower_limits, top_limits, point,
                                           next_cumulative_radius,
                                           square_radius, dimension + 1)
        return items

# Closest Pair
# Order by x coordinate
# divide up in half etc etc. Find minimum of distances between left, right, and split
import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, point2):
        return math.sqrt(point2.x * point2.x + point2.y * point2.y)
        
    def __repr__(self):
        return "(%i, %i)" % (self.x, self.y)

def closest_helper(sorted_pt_array):
    arr1, arr2 = split_array(sorted_pt_array)
    
    # Base case
    if len(sorted_pt_array) <= 3:
        min_pt, pt = arr2[0], arr1[0]
        min_dist = pt.distance_to(min_pt)
        
        for i in xrange(1, len(arr2)):
            dist = pt.distance_to(arr2[i])
            if dist < min_dist:
                min_pt, min_dist = arr2[i], dist
        
        return (pt, min_pt, min_dist)
    else:
        pt1, pt12, dist1 = closest_helper(arr1)
        pt2, pt22, dist2 = closest_helper(arr2)
        combos = [(pt1, pt2, pt1.distance_to(pt2)), (pt12, pt22, pt12.distance_to(pt22)), (pt1, pt22, pt1.distance_to(pt22)), (pt12, pt2, pt12.distance_to(pt2)), (pt1, pt12, dist1), (pt2, pt22, dist2)]
        return min(combos, key=lambda x: x[-1])
        
    
def split_array(array):
    split_pt = (len(array) / 2)
    return (array[:split_pt], array[split_pt:])

def closest_pairs(pt_array):
    if len(pt_array) > 1:
        return closest_helper(sorted(pt_array, key=lambda pt: pt.x))
    else:
        return []


pts = [Point(6,7), Point(3, 4), Point(-2, 3), Point(-2, -1), Point(4, 6)]

print(closest_pairs(pts))
    
    
from typing import Tuple

def compute_line_intersection(p0:Tuple[float, float],
                              p1:Tuple[float, float],
                              p2:Tuple[float, float],
                              p3:Tuple[float, float])->Tuple[bool, Tuple[float, float]]:
    """
    Compute line intersection https://stackoverflow.com/a/1968345 
    """
    s1 = (p1[0] - p0[0], p1[1] - p0[1])
    s2 = (p3[0] - p2[0], p3[1] - p2[1])

    z = -s2[0] * s1[1] + s1[0] * s2[1]
    if z == 0:
        return False, None
    
    s = (-s1[1] * (p0[0] - p2[0]) + s1[0] * (p0[1] - p2[1])) / z
    t = ( s2[0] * (p0[1] - p2[1]) - s2[1] * (p0[0] - p2[0])) / z

    if 0 <= s <= 1 and 0 <= t <= 1:
        return True, (p0[0] + (t * s1[0]), p0[1] + (t * s1[1]))
    else:
        return False, None

if __name__ == "__main__":
    from matplotlib import pyplot as plt
    
    pt0 = (0.0, 0.0)
    pt1 = (10.0, 10.0)
    pt2 = (5.0, 0.0)
    pt3 = (0.0, 5.0)
    intersection_ok, intersection_pt = compute_line_intersection(pt0, pt1, pt2, pt3)
    
    # draw
    plt.plot([pt0[0], pt1[0]], [pt0[1], pt1[1]])
    plt.plot([pt2[0], pt3[0]], [pt2[1], pt3[1]])
    if intersection_ok:
        plt.plot([intersection_pt[0]], [intersection_pt[1]], '*')
    plt.show()
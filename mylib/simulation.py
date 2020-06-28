from mylib.util import compute_line_intersection

from typing import Tuple, List
from collections import namedtuple
import numpy as np

ScanData = namedtuple('ScanData', ['angle', 'distance'])


class Simulation:
    def __init__(self, angle_start=0.0, angle_end=360.0, angle_step=1.0, lidar_range=25000.0):
        self.angle_start = angle_start
        self.angle_end = angle_end
        self.angle_step = angle_step
        self.lidar_range = lidar_range

    def set_map_data(self, map_data: List[Tuple[float, float, float, float]]):
        self.map_data = map_data

    def scan(self, curr_pos: Tuple[float, float], visualize_raycast: bool = False) -> List[ScanData]:
        """
        Given current position and angle, return the list of ScanData
        """
        if self.map_data is None:
            raise Exception("map_data is empty, "
                            "please use set_map_data to set it")

        curr_x = curr_pos[0]
        curr_y = curr_pos[1]

        result = list()
        for angle in np.arange(self.angle_start, self.angle_end, self.angle_step):
            v_x = np.sin(np.deg2rad(90+angle)) * self.lidar_range
            v_y = np.cos(np.deg2rad(90+angle)) * self.lidar_range

            distances = list()
            vis_datas = list()  # data for visualizing intersection
            for x1, y1, x2, y2 in self.map_data:
                hit_ok, hit_result = compute_line_intersection(
                    (curr_x, curr_y), (curr_x + v_x, curr_y + v_y), (x1, y1), (x2, y2))
                if not hit_ok:
                    continue

                dist = self._compute_dist(
                    curr_x, curr_y, hit_result[0], hit_result[1])
                distances.append(dist)
                if visualize_raycast:
                    # Add all required data for visualizing intersection
                    vis_datas.append(
                        [hit_result, angle, curr_x, curr_y, v_x, v_y, x1, y1, x2, y2])

            if len(distances) == 0:
                continue

            # If there are multiple intersection, choose the one with the closest distance to (curr_x, curr_y)
            min_idx = np.argmin(distances)
            result.append(ScanData(angle, distances[min_idx]))

            if visualize_raycast:
                self._visualize_point_intersection(vis_datas[min_idx])

        return result

    def _compute_dist(self, x1: float, y1: float, x2: float, y2: float):
        """
        Compute euclidean distance
        """
        dx = x1 - x2
        dy = y1 - y2
        dist = np.sqrt(dx*dx + dy*dy)
        return dist

    def _visualize_point_intersection(self, data):
        """
        Visualize point intersection and lines
        """
        from matplotlib import pyplot as plt
        hit_result, angle, curr_x, curr_y, v_x, v_y, wall_x1, wall_y1, wall_x2, wall_y2 = data

        # Draw raycast with color red
        plt.plot([curr_x, curr_x + v_x],
                 [curr_y, curr_y + v_y], c='r')

        # Draw wall with color blue
        plt.plot([wall_x1, wall_x2], [wall_y1, wall_y2], c='b')

        # Draw intersection
        plt.plot([hit_result[0]], [hit_result[1]], '*')

        # Draw all walls
        for x1, y1, x2, y2 in self.map_data:
            plt.plot([x1, x2], [y1, y2], c='black')

        plt.suptitle("angle = %d" % angle)
        plt.show()

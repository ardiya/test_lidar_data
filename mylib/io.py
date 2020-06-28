import numpy as np
from typing import List
from typing import Tuple


def read_trajectories(filename: str, scale_factor: float = 1.0) -> List[np.array]:
    """
    Read trajectories from file and return it as list of 3x3 transformation matrix
    """
    result = list()
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if line == "":
                break
            # sweep_id, n = [int(x) for x in line.split(",")] # The data format is pretty useless
            line = fp.readline()
            x, y = [float(a) for a in line.split(",")]
            pt = [[1.0, 0.0, x],
                  [0.0, 1.0, y],
                  [0.0, 0.0, 1.0]]
            result.append(np.array(pt))

    return result


def read_lidar(filename: str, scale_factor=1.0/1000.0,
               lidar_range: Tuple[float, float] = [0.01, 10000.0]) -> List[np.array]:
    """
    Read lidar sweep data from file and return it as list of nx3x3 numpy array
    note: the provided test data was weird, lidar_transform is used to convert y to -y
    """
    result = list()
    with open(filename, "r") as fp:
        while True:
            line = fp.readline()
            if line == "":
                break
            _, n = [int(x) for x in line.split(",")]
            lidar_points = []
            for _ in range(n):
                line = fp.readline()
                angle, dist = [float(x) for x in line.split(",")]
                if not lidar_range[0] <= dist <= lidar_range[1]:
                    continue
                x = np.cos(np.deg2rad(angle)) * dist * scale_factor
                y = np.sin(np.deg2rad(angle)) * dist * scale_factor
                pt = np.array([[1.0, 0.0, x],
                               [0.0, 1.0, y],
                               [0.0, 0.0, 1.0]])
                lidar_points.append(pt)
            result.append(np.array(lidar_points))
    return result


if __name__ == "__main__":
    trajectories = read_trajectories("data/FlightPath.csv")
    assert type(trajectories) == list
    assert len(trajectories) > 0
    for traj in trajectories:
        assert type(traj) == type(np.array([]))
        assert traj.shape == (3, 3)

    lidar_data = read_lidar("data/LIDARPOINTS.csv")
    assert type(lidar_data) == list
    assert len(lidar_data) > 0
    for points in lidar_data:
        assert type(points) == type(np.array([]))
        assert len(points.shape) == 3
        assert points.shape[1:] == (3, 3)

import numpy as np
from typing import List


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


if __name__ == "__main__":
    trajectories = read_trajectories("data/FlightPath.csv")
    assert type(trajectories) == list
    assert len(trajectories) > 0
    for traj in trajectories:
        assert type(traj) == type(np.array([]))
        assert traj.shape == (3, 3)

from mylib.io import read_map, read_trajectories, write_map
from mylib.util import compute_line_intersection
from mylib.simulation import Simulation

import numpy as np
from collections import namedtuple

ScanData = namedtuple('ScanData', ['angle', 'distance'])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--map_path", type=str,
                        default="data/extra/Mapping.csv")
    parser.add_argument("-t", "--trajectories", type=str,
                        default="data/FlightPath.csv")
    parser.add_argument("-o", "--lidar_out", type=str,
                        default="data/extra/LIDARPoints.csv")
    parser.add_argument("--angle_start", type=float, default=0.0)
    parser.add_argument("--angle_end", type=float, default=360.0)
    parser.add_argument("--angle_step", type=float, default=1.0)
    parser.add_argument("--lidar_range", type=float, default=25000.0)  # mm
    parser.add_argument("--visualize_raycast", type=bool, default=False)

    args = parser.parse_args()

    map_data = read_map(args.map_path,)
    sim = Simulation(angle_start=args.angle_start, angle_end=args.angle_end,
                     angle_step=args.angle_step, lidar_range=args.lidar_range)
    sim.set_map_data(map_data)

    all_trajectories_scan = list()
    trajectories_data = read_trajectories(args.trajectories, scale_factor=1000)
    for i, traj in enumerate(trajectories_data):
        traj_x = traj[0, 2]
        traj_y = traj[1, 2]
        scan_data = sim.scan((traj_x, traj_y), visualize_raycast=args.visualize_raycast)
        all_trajectories_scan.append(scan_data)
    
    write_map(args.lidar_out, all_trajectories_scan)
    print("Map written in", args.lidar_out, ". Total sweep:", len(all_trajectories_scan))

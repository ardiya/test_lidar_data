from mylib.io import read_trajectories, read_lidar
from mylib.visualization import Visualizer

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--lidar_path", type=str,
                        default="data/LIDARPoints.csv")
    parser.add_argument("-t", "--trajectories", type=str,
                        default="data/FlightPath.csv")
    args = parser.parse_args()

    # Read all required data
    lidar_points = read_lidar(args.lidar_path)
    trajectories = read_trajectories(args.trajectories)

    # Visualize data
    vis = Visualizer()
    vis.set_lidar_data(lidar_points)
    vis.set_trajectories(trajectories)
    vis.show()

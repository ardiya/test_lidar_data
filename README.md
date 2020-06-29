# Test Lidar Data

## Installation
```
pip3 install -r requirements.txt
```

## Running the program

### Visualization
For running the visualization, you would need 2 data: flight path and the lidar points.

Usage: `python3 main_visualization.py [--lidar_path "/path/to/LIDARPoints.csv"] [--trajectories "/path/to/FlightPath.csv"]`

Example for visualizing default data
```
python3 main_visualization.py --lidar_path "data/LIDARPoints.csv" --trajectories "data/FlightPath.csv"
```
If you run the example above, you should be able to see the following animation

![visualization1](https://raw.githubusercontent.com/ardiya/test_lidar_data/master/img/vis1.gif)
There are 3 parts in the visualization:
- The title shows the current `frameID`
- The left area shows the current lidar data
  - The red point denotes the drone position as the center(0, 0)
  - The black point denotes the lidar scan. When the `frameID` is changed, the lidar scan of the `frameID` will be shown
- The right area shows the combined lidar data.
  - The colorful points denotes the map. Different color means that the map is seen from different `frameID`
  - The `X` marker denotes the position of the drone in the map. When the `frameID` is changed, the drone position is updated.

### Simulation
For running the simulation, you would need 2 data: flight path and mapping data.

Usage:

```
python3 main_simulation.py
    [--map_path "/path/to/mapping.csv"] 
    [--trajectories "/path/to/FlightPath.csv"]
    [--lidar_out "/path/to/LidarPoints.csv"]
    [--angle_start 0.0]
    [--angle_end 360.0]
    [--angle_step 1.0]
    [--lidar_range 25000.0]
```

Example for saving mapping data and then visualize the result

```
OUT_PTH=out_points.csv
python3 main_simulation.py --map_path "data/extra/Mapping.csv" --trajectories "data/FlightPath.csv" --lidar_out $OUT_PTH && python3 main_visualization.py --lidar_path $OUT_PTH --trajectories "data/FlightPath.csv"
```
If you run the example above, you should be able to see the following animation

![visualization2](https://raw.githubusercontent.com/ardiya/test_lidar_data/master/img/vis2.gif)

## Discussion
- This code represents the drone pose as numpy 3x3 matrix and the lidar scans as numpy nx3x3 matrix, this way it's easy to do transformation using numpy's @(matmul) operation
- Visualization is done with matplotlib's animation function.
- In the lidar scan simulation
  - To do lidar scan simulation, a sweep(with multiple angle) is performed for each drone pose
  - The sweep is basically raytracing from the drone position and the angle of the sweep and stop if we hit the wall using [Bressenham's algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm). In this code, the raytracing is done using line-line intersection as [seen in this part of code](https://github.com/ardiyahttps://github.com/ardiya/test_lidar_data/blob/master/mylib/util.py#L3-L23/test_lidar_data/blob/master/mylib/util.py#L3-L23)
    - If the map data is represented as the GridMap(2D matrix), it would makes more sense to use the Bressenham's algorithm.
    - If the map is represented with multiple walls(x1, y1, x2, y2), the line-line intersection would perform better.

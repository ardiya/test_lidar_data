# Test Lidar Data

## Installation
```
pip3 install -r requirements.txt
```

## Running the program

### Visualization
For running the visualization, you would need 2 data: flight path and the lidar points.

Usage: `python3 main_visualization.py [--lidar_path "/path/to/LIDARPoints.csv"] [--trajectories "/path/to/FlightPath.csv"]`

Example Loading default data
```
python3 main_visualization.py --lidar_path "data/LIDARPoints.csv" --trajectories "data/FlightPath.csv"
```

### Simulation
For running the simulation, you would need 2 data: flight path and mapping data.

Usage:

```
python3 main_simulation.py
    [--map_path "/path/to/mapping.csv"] 
    [--trajectories "/path/to/FlightPath.csv"]
    [--angle_start 0.0]
    [--angle_end 360.0]
    [--angle_step 1.0]
    [--lidar_range 25000.0]
```

Example loading default data

```
python3 main_simulation.py --map_path "data/extra/Mapping.csv" --trajectories "data/FlightPath.csv"
```

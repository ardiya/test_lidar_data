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

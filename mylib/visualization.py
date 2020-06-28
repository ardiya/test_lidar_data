from typing import List
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np


class Visualizer:
    LIDAR_RANGE = 20.0  # meter, TODO: Automatically determine based on the input
    T_VIS = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])  # TODO: clarify data

    def __init__(self):
        pass

    def set_trajectories(self, trajectories: List[np.array]):
        self.trajectories = trajectories

    def set_lidar_data(self, lidar_data: List[np.array]):
        self.lidar_data = lidar_data

    def _configure_combined_lidar(self):
        """
        Configure the subplot
        return the objects that will be updated during animation_update
        """
        self.colors = np.random.rand(len(self.lidar_data), 3)
        # Draw line plotting drone trajectories
        self.ax_lidar_comb.plot([traj[0, 2] for traj in self.trajectories],
                                [traj[1, 2] for traj in self.trajectories],
                                linewidth=1, c=(0, 0, 0, 0.5))
        # Draw the points denoting wall with different color
        for i, (pts, T) in enumerate(zip(self.lidar_data, self.trajectories)):
            new_pts = T @ self.T_VIS @ pts
            self.ax_lidar_comb.scatter(new_pts[:, 0, 2], new_pts[:, 1, 2],
                                       marker='o', s=1, c=[self.colors[i]])
        # create dummy for position in combined subplot
        comb_pts = self.ax_lidar_comb.plot([], [], marker='x', markersize=12)
        comb_pts = comb_pts[0]

        return comb_pts
    
    def _configure_current_lidar_subplot(self):
        """
        Configure the subplot
        return the objects that will be updated during animation_update
        """
        self.ax_curr.axis([-self.LIDAR_RANGE, self.LIDAR_RANGE,
                           -self.LIDAR_RANGE, self.LIDAR_RANGE])
        # draw (0, 0) in red color
        self.ax_curr.scatter([0], [0], color='red')
        # create dummy for lidar_points in current subplot
        curr_pts = self.ax_curr.scatter([], [], color='black')
        
        return curr_pts

    def show(self):
        if self.lidar_data is None:
            raise Exception(
                "lidar_data is empty, please use set_lidar_data to set it")
        if self.trajectories is None:
            raise Exception(
                "trajectories is empty, please use set_trajectories to set it")
        if len(self.trajectories) != len(self.lidar_data):
            raise Exception("len(trajectories) and len(lidar_data) are different. "
                            "Please make sure you use the correct data")

        # Create figure, left(curr lidar) and right(combined lidar)
        self.fig, (self.ax_curr, self.ax_lidar_comb) = plt.subplots(1, 2)
        comb_pts = self._configure_combined_lidar()
        curr_pts = self._configure_current_lidar_subplot()

        # Start animation
        _ = animation.FuncAnimation(self.fig, self._update_animation,
                                    frames=range(len(self.lidar_data)),
                                    fargs=(curr_pts, comb_pts),
                                    interval=1000)
        plt.show()

    def _update_animation(self, i, curr_pts, comb_pts):
        # Update title
        self.fig.suptitle('Frame - %d' % i)

        # Update the current trajectory in combined lidar
        traj = self.trajectories[i]
        comb_pts.set_xdata([traj[0, 2]])
        comb_pts.set_ydata([traj[1, 2]])
        comb_pts.set_color(self.colors[i])

        # Update points in the current lidar
        pts = self.lidar_data[i]
        curr_pts.set_offsets(pts[:, :2, 2])

        return curr_pts,

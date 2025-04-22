import cv2
import matplotlib.pyplot as plt
import numpy as np
#
lidar_path = "C:/Users/chari/Desktop/lidar/camera_lidar/20180810_150607/lidar/cam_front_center/20180810150607_lidar_frontcenter_000000060.npz"
lidar_data = np.load(lidar_path)

# print("Available keys in NPZ:")
# print(lidar_data.files)

points = lidar_data['pcloud_points']  # (N, 3)

# === Plot Top-Down View (Bird's Eye) ===
x = points[:, 0]  # forward
y = points[:, 1]  # lateral (left/right)

plt.figure(figsize=(10, 8))
plt.scatter(x, y, c='black', s=0.1)
plt.title("Lidar Point Cloud (Top-Down View)")
plt.xlabel("X (Forward)")
plt.ylabel("Y (Left/Right)")
plt.grid(True)
plt.axis("equal")
plt.show()

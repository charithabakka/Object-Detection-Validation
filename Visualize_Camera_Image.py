import cv2
import matplotlib.pyplot as plt

img_path = "C:/Users/chari/Desktop/lidar/camera_lidar/20180810_150607/camera/cam_front_center/20180810150607_camera_frontcenter_000000060.png"
image = cv2.imread(img_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(12, 6))
plt.imshow(image)
plt.title("Front Center Camera Image")
plt.axis("off")
plt.show()
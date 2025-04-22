import cv2
import matplotlib.pyplot as plt

def load_image(image_path):
    return cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

def load_labels(label_path):
    boxes = []
    with open(label_path) as f:
        for line in f:
            parts = line.split()
            if parts[0] != 'Car':  # Only validate "Car" class
                continue
            xmin, ymin, xmax, ymax = map(float, parts[4:8])
            boxes.append((xmin, ymin, xmax, ymax))
    return boxes

# Fake detection: Shift boxes a little
def generate_fake_detections(gt_boxes):
    return [(x+5, y+5, x2+5, y2+5) for (x, y, x2, y2) in gt_boxes]

def draw_boxes(image, boxes, color=(0, 255, 0)):
    for (x, y, x2, y2) in boxes:
        cv2.rectangle(image, (int(x), int(y)), (int(x2), int(y2)), color, 2)
    return image

img = load_image("kitti/images/000001.png")
gt = load_labels("kitti/labels/000001.txt")
det = generate_fake_detections(gt)

img_gt = draw_boxes(img.copy(), gt, (0, 255, 0))  # Green = Ground Truth
img_det = draw_boxes(img.copy(), det, (255, 0, 0))  # Blue = Detection

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1)
plt.title("Ground Truth")
plt.imshow(img_gt)
plt.subplot(1, 2, 2)
plt.title("Fake Detections")
plt.imshow(img_det)
plt.show()
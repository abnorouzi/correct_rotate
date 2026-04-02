import cv2
from imutils import rotate_bound
import matplotlib.pyplot as plt
import argparse
import os

# ---------------------------
# 1.reading image path from terminal
# ---------------------------
parser = argparse.ArgumentParser(description="Compare simple OpenCV rotation vs rotate_bound from imutils")
parser.add_argument("image_path", type=str, help="Path to input image")
parser.add_argument("--angle", type=float, default=45, help="Rotation angle in degrees")
args = parser.parse_args()

if not os.path.exists(args.image_path):
    print(f"Error: File '{args.image_path}' does not exist.")
    exit(1)

image = cv2.imread(args.image_path)
if image is None:
    print(f"Error: Could not read image '{args.image_path}'.")
    exit(1)

# ---------------------------
# 2. simple rotatio eith OpenCV (cut-off)
# ---------------------------
def rotate_simple(img, angle):
    (h, w) = img.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))  # اندازه خروجی همان اندازه اصلی
    return rotated

rotated_cutoff = rotate_simple(image, args.angle)

# ---------------------------
# 3. solution rotate_bound
# ---------------------------
rotated_fixed = rotate_bound(image, args.angle)

# ---------------------------
# 4. showing the diferences
# ---------------------------
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Rotated (cut-off)")
plt.imshow(cv2.cvtColor(rotated_cutoff, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Rotated (fixed)")
plt.imshow(cv2.cvtColor(rotated_fixed, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()

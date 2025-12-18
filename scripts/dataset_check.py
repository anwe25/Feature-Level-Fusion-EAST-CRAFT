import os
import cv2
import sys
from glob import glob

# Try multiple ways to locate the dataset so script does not depend on CWD.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

candidates = [
    os.path.join(PROJECT_ROOT, "data", "icdar2015", "ch4_training_images"),
    os.path.join(SCRIPT_DIR, "..", "data", "icdar2015", "ch4_training_images"),
    os.path.join(os.getcwd(), "data", "icdar2015", "ch4_training_images"),
    os.path.join(os.getcwd(), "ch4_training_images"),
]

IMG_DIR = None
for c in candidates:
    c_abs = os.path.abspath(c)
    if os.path.isdir(c_abs):
        IMG_DIR = c_abs
        break

# Ground truth dir relative to chosen IMG_DIR or project root
if IMG_DIR:
    GT_DIR = os.path.join(os.path.dirname(IMG_DIR), "ch4_training_localization_transcription_gt")
else:
    GT_DIR = os.path.join(PROJECT_ROOT, "data", "icdar2015", "ch4_training_localization_transcription_gt")

print("Script location:", SCRIPT_DIR)
print("Working directory:", os.getcwd())
print("Resolved IMG_DIR:", IMG_DIR if IMG_DIR else "(not found)")
print("Resolved GT_DIR:", os.path.abspath(GT_DIR))

if IMG_DIR is None:
    print("IMG_DIR not found. Tried the following locations:")
    for p in candidates:
        print(" -", os.path.abspath(p))
    print("Contents of project root:", sorted(os.listdir(PROJECT_ROOT)))
    sys.exit(1)

# Collect images with common extensions (case-insensitive)
exts = ["*.jpg", "*.jpeg", "*.png", "*.bmp", "*.tif", "*.tiff"]
images = []
for e in exts:
    images.extend(sorted(glob(os.path.join(IMG_DIR, e))))
    images.extend(sorted(glob(os.path.join(IMG_DIR, e.upper()))))

images = sorted(set(images))  # dedupe & sort

print("Total training image files found (any ext):", len(images))

if not images:
    print("No image files found in", IMG_DIR)
    print("Directory listing:", sorted(os.listdir(IMG_DIR)))
    sys.exit(1)

# Use first image
img_path = images[0]
img_name = os.path.basename(img_path)

# Corresponding GT file (adjust naming if needed)
gt_name = "gt_" + img_name.rsplit(".", 1)[0] + ".txt"
gt_path = os.path.join(GT_DIR, gt_name)

print("Sample image:", img_name)
print("GT file expected:", gt_name)

img = cv2.imread(img_path)
if img is None:
    print("Image not loaded — check OpenCV support and file path:", img_path)
    sys.exit(1)

print("Image loaded successfully, shape:", img.shape)

if os.path.exists(gt_path):
    print("Ground truth file found:", gt_path)
else:
    print("Ground truth file missing (expected):", gt_path)

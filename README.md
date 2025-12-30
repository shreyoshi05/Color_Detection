# Color Detection using OpenCV 🎨

This project demonstrates basic color detection using OpenCV with real-time webcam detection.
It detects a specific color range in an image using HSV color space
and highlights the detected regions.

## Concepts Used
- BGR to HSV conversion
- Color thresholding
- Masking
- Contour detection
- Drawing bounding boxes

## How it Works
1. Convert image from BGR to HSV
2. Define lower and upper HSV color range
3. Create mask using `cv2.inRange`
4. Detect contours on the mask
5. Draw contours on the original image

## Tools
- Python
- OpenCV
- NumPy

## Status
Beginner project created as part of learning OpenCV fundamentals.

## Future Improvements
- Trackbars for dynamic color selection
- Support for multiple colors

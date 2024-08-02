## Installation
1. Install [ultralytics](https://docs.ultralytics.com/quickstart/)
## Gun Detector Model
For generating gun detection model, yolov8n model is fine tune on custom dataset. The model details is [here.](https://github.com/affanrasheed/Gun-Detector-Yolov8/tree/main/Training_Testing)

## Gun Cropping Explanation
1. Download gun detector model
2. Capture input video using opencv
3. Run gun detector model on each captured frame
4. Detect the gun 
5. Blur the gun from the frame using the detections with the help of opencv blur function


## Output Results
[Test Video for Gun Blurring](https://drive.google.com/file/d/1cmeNvc-8m-AJ57cVMLRtolah88CGxVy3/view?usp=sharing)


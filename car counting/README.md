## Installation
1. Install [ultralytics](https://docs.ultralytics.com/quickstart/)
## Car Counting Explanation
1. Download Yolov8n.pt pretrained model
2. Capture input video using opencv
3. Run yolov8n on each captured frame
4. Detect specific "car" class
5. Track car class using bo-sort
6. Count the car object using ObjectCounter in Yolo solutions
7. Counting is performed when a car object cross a line

## Output Results
The output will look like this:

![alt-text](car_counting_output2.gif)

Complete Video

[Test Video for Car Counting](https://drive.google.com/file/d/1tP2ApawUHPl-GSNfUpedpxcTbQWaMGHB/view?usp=sharing)

## Possible Improvements
1. As only one class is counting so yolov8 model can be optimize for a single class.
2. Model can be fine tune to get better results
3. Graph Optmization, pruning, knowledge distillation and quantization can be performed for better speed.

## Installation
1. Install [ultralytics](https://docs.ultralytics.com/quickstart/)

## Region Counting and Blurring
In this tutorial, a class object can be counted in a given region and blur a specific class object depending on user input.

## Running Instructions
1. By default, all the objects will be counted inside a given and no blurring of object
   ```bash
   python3 region_counting.py --source "traffic3.mp4" --save-img --view-img --device 0
   ```
2. Blurring only the person object
   ```bash
   python3 region_counting.py --source "traffic3.mp4" --save-img --view-img --device 0 --blur-class person
   ```
3. Blurring person and car object
   ```bash
   python3 region_counting.py --source "traffic3.mp4" --save-img --view-img --device 0 --blur-class person,car
   ```
4. Blurring all detected object in a region
   ```bash
   python3 region_counting.py --source "traffic3.mp4" --save-img --view-img --device 0 --blur-class ALL
   ```
      
## Output Results
### For No Blurring
![alt-txt](no_blur.gif)

complete video
[Test Video for No Blur](https://drive.google.com/file/d/103iMTAyS43c7WpTJSubGDx-YfqakS2PM/view?usp=sharing)
### For Blurring Car Object
![alt-txt](blur_person.gif)

complete video
[Test Video for Person Object Blur](https://drive.google.com/file/d/1Np89A1yAXgi4duxPhO5BqpIlxXYlWdac/view?usp=sharing)
### For Blurring Car and Person
![alt-txt](blur_person_car.gif)

complete video
[Test Video for Person and Car Object Blur](https://drive.google.com/file/d/1cLnEOZdHCVDd1vEJBmKUJ6F6vgjCJfgU/view?usp=sharing)
### For Blurring All Detected Object
![alt-txt](blur_all.gif)

complete video
[Test Video for Blur all Object](https://drive.google.com/file/d/1RZTFqVnYbRDxC8FYhR6kOho9tcmigwh7/view?usp=sharing)

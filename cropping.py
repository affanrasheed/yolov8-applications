import os

import cv2

from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

model = YOLO("best.pt")
names = model.names

cap = cv2.VideoCapture("cctv_video.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

crop_dir_name = "ultralytics_crop3 "

if not os.path.exists(crop_dir_name):
    os.mkdir(crop_dir_name)


# Video writer
video_writer = cv2.VideoWriter("object_cropping_output4.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

idx = 0

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    #results = model.predict(im0, show=False)
    results = model.track(im0, persist=True, show=False, conf=0.32)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    annotator = Annotator(im0, line_width=2, example=names)

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            idx += 1
            annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])

            crop_obj = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]

            if not os.path.exists(crop_dir_name+"/"+names[int(cls)]):
                os.mkdir(crop_dir_name+"/"+names[int(cls)])
            cv2.imwrite(os.path.join(crop_dir_name+"/"+names[int(cls)], str(idx) + ".png"), crop_obj)

    cv2.imshow("ultralytics", im0)
    video_writer.write(im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
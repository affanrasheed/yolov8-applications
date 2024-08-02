import cv2

from ultralytics import YOLO, solutions

model = YOLO("yolov8n-pose.pt")
cap = cv2.VideoCapture("squats_test.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter("workouts.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
pose_up_thre = 145
pose_down_thre = 95 #threshold angles
point = [14,12,6]    #point to monitor (vary for specific exercise)
gym_object = solutions.AIGym(
    line_thickness=2,
    view_img=True,
    pose_type="squat",
    kpts_to_check=point,
    pose_up_angle = pose_up_thre,
    pose_down_angle=pose_down_thre
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    results = model.track(im0, verbose=False)  # Tracking recommended
    # results = model.predict(im0)  # Prediction also supported
    im0 = gym_object.start_counting(im0, results)
    video_writer.write(im0)

cv2.destroyAllWindows()
video_writer.release()
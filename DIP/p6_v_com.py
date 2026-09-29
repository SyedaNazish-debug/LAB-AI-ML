import cv2
import numpy as np
import os

in_video= "sunrise.mp4"
out_video="compressed_video.mp4"

cap=cv2.VideoCapture(in_video)

if not cap.isOpened():
    print("error:Video not found")
    exit()
original_w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

original_fps=cap.get(cv2.CAP_PROP_FPS)

new_w=original_w//2
new_h=original_h//2

new_fps=original_fps/2

fourcc=cv2.VideoWriter_fourcc(*"mp4v")

out=cv2.VideoWriter(
    out_video,
    fourcc,
    new_fps,
    (new_w,new_h)
)

while True:
    ret, frame=cap.read()

    if not ret:
        break

    resized_fr=cv2.resize(
        frame,
        (new_w,new_h)
    )

    out.write(resized_fr)

cap.release()
cap.release()

cv2.destroyAllWindows()

if os.path.exists(in_video) and os.path.exists(out_video):

    original_s=os.path.getsize(in_video)
    compressed_s=os.path.getsize(out_video)

    print("Original video size:",original_s/(1024*1024),"MB")
    print("compressed video size:",compressed_s/(1024*1024),"MB")

    print("Video comppression completed sucessfully")
import cv2
import os

def set_writer(f, fourcc, shape):
    return cv2.VideoWriter("new_"+f, fourcc, 20, shape)

for file in os.listdir('./'):
    if file[-3:] != "avi":
        continue
    cap = cv2.VideoCapture(file)
    fourcc = cv2.VideoWriter_fourcc(*'XVID') 
    writer = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if writer is None:
            writer = set_writer(file, fourcc, (frame.shape[1], frame.shape[0]))

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        writer.write(rgb)
     
    cap.release()
    writer.release()



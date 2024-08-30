# 이미지로부터 영상 생성
import requests
import os
import cv2
import numpy as np


def create_video(image_folder, output_video='video.avi', frame_rate=1):
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'DIVX'), frame_rate, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

create_video('./')  # 현재 폴더의 이미지를 사용하여 비디오 생성



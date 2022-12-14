# -*- coding: utf-8 -*-
"""mediapipe_final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aeW-Vt-Yg-3uTns8v_OZWJ5yr7kf_Q3h
"""

!pip install numpy==1.19.3
!pip install mediapipe

from google.colab import files

uploaded = files.upload()

import mediapipe as mp
import cv2

import numpy as np
#C:\\Users\\hongik\\Desktop\\test_video\\video1
# Read images with OpenCV.
file_path='C:\\Users\\hongik\\Desktop\\test_video\\video1\\'
for i in range(15):
    images = {str(i):cv2.imread(file_path+str(i)+'.jpg')}  
 #{name: cv2.imread(name) for name in uploaded.keys()}
    # Initialize MediaPipe Pose.
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(
        static_image_mode=True, min_detection_confidence=0.5)

    # Prepare DrawingSpec for drawing the face landmarks later.
    mp_drawing = mp.solutions.drawing_utils 
    drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=2)

    photo_return_value=[]
    for name, image in images.items():
      # Convert the BGR image to RGB and process it with MediaPipe Pose.
        results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
      # landmark 출력
        image_hight, image_width, _ = image.shape
        if not results.pose_landmarks:
            continue

      #오른쪽 무릎, 오른쪽 엉덩이 좌표 비교하고 리스트에 0또는 1저장
        right_knee = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_KNEE].y * image_width
        right_hip = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_HIP].y * image_width
        print(right_knee-right_hip)
        if right_knee > right_hip:
            photo_return_value.append(0)
        else:
            photo_return_value.append(1)

      # Draw pose landmarks.
        print(f'Pose landmarks of {name}:')
        annotated_image = image.copy()
        mp_drawing.draw_landmarks(
            image=annotated_image,
            landmark_list=results.pose_landmarks,
            connections=mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=drawing_spec,
            connection_drawing_spec=drawing_spec)
        cv2.imshow('dd',annotated_image)

      #photo_return_value 출력
        print(f'photo_return_value 출력(1은 풀스쿼트) : {photo_return_value}')

    #만들고 싶은 느낌
    """
    if '1' in photo_return_value:
      return 1
    else: 
      return 0
    """


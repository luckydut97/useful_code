import cv2

# video 경로
vidcap = cv2.VideoCapture('.\\Video\\sample.mp4')

count = 0

while (vidcap.isOpened()):

    ret, image = vidcap.read()

    # 시간 설정, 30=1초 정도, 숫자 더 높이면 초 늘어남
    if (int(vidcap.get(1)) % 60 == 0):
        print('Saved frame number : ' + str(int(vidcap.get(1))))
        # 이미지 경로와 파일명
        cv2.imwrite(".\\Image\\%d.jpg" % count, image)
        print('Saved frame%d.jpg' % count)
        count += 1

vidcap.release()
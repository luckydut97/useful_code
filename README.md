# useful_code_python
A collection of short and simple useful codes (Python)
<br>
--
<br>
1. video_frame_cut.py
<br><br>
비디오 파일을 지정한 프레임 간격으로 자동으로 스크린샷을 생성하는 코드입니다.
<br><br>
2. full_squat.py

![image](https://user-images.githubusercontent.com/82084402/216262803-d3f88cb1-c4ef-4a2a-8874-97e0f3e80df4.png)

<br><br>
사용자가 스쿼트를 한 번 수행할때, 1초 단위의 사진들을 분석해서 풀스쿼트인지 아닌지 판별합니다.
<br>
구글에서 제공하는 AI 프레임워크인 Mediapipe를 활용하였습니다. 
<br>
Mediapipe 에서는 비디오형식 데이터를 이용한 다양한 비전 AI 기능을 파이프라인 형태로 손쉽게 사용할 수 있도록 제공됩니다. 1번의 video_frame_cut.py 로 사용자의 스쿼트 동영상을 사진으로 분할한 후 저장한 디렉토리를 full_squat.py에서 경로로 설정하면 됩니다.

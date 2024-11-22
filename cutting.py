from PIL import Image
import os

# 현재 작업 디렉토리의 경로 확인
current_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 파일 경로 설정
image_path = os.path.join(current_dir, 'image.png')

# 이미지 불러오기
image = Image.open(image_path)

# RGBA를 RGB로 변환
if image.mode in ('RGBA', 'P'):
    image = image.convert('RGB')

# 8열 3행으로 나누기 위한 좌표 계산
width, height = image.size
crop_width = width // 8
crop_height = height // 3

# 결과물을 저장할 폴더 생성
output_dir = os.path.join(current_dir, 'cropped_images')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 각 격자별로 이미지 자르기
for row in range(3):
    for col in range(8):
        left = col * crop_width
        upper = row * crop_height
        right = left + crop_width
        lower = upper + crop_height
        cropped_image = image.crop((left, upper, right, lower))
        # 잘린 이미지를 RGB로 변환하여 저장
        output_path = os.path.join(output_dir, f'cropped_image_{row * 8 + col + 1}.jpg')
        cropped_image.save(output_path)
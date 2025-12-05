import shutil
import os

# 1. 원본이 될 더미 이미지 이름 (폴더에 미리 넣어두세요)
source_file = "base.png" 

# 2. 필요한 파일 리스트
required_files = [
    "moak.png", "jiri.png", "naejang.png", "maee.png",
    "byeonsan.png", "seonyudo.png", "mohang.png", "goosipo.png",
    "deokjin.png", "kwanghanroo.png", "kyeongki.png", "gochang.png"
]

# 3. 복사 시작
for file_name in required_files:
    shutil.copyfile(source_file, file_name)
    print(f"✅ Created: {file_name}")

print("\n🎉 모든 이미지 생성 완료!")
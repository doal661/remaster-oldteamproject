from fastapi import FastAPI
import json

app = FastAPI()

# test 주석 // remaster-oldteamproject


# JSON 파일 로드
with open('test-data.json', 'r', encoding='utf-8') as f:
    Informations = json.load(f)

# 사용법은 기존 딕셔너리와 똑같습니다!
print(Informations["모악산"])

@app.get("/places")
def get_places():
    return Informations
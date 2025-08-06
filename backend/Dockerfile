# 1. Python 베이스 이미지 선택
FROM python:3.11-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 4. 소스코드 복사 (docker-compose에서 볼륨 마운트 할 예정이라 이 부분은 빌드 시에는 주석 처리해도 무방)
COPY . /app

# 5. uvicorn 서버 실행 (라이브 리로딩 활성화)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
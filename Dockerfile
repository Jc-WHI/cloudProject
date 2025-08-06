# Dockerfile

# 1. 베이스 이미지 선택: Python 3.11 버전을 사용합니다.
FROM python:3.11-slim

# 2. 작업 디렉토리 설정: 컨테이너 내에서 코드가 위치할 폴더를 지정합니다.
WORKDIR /app

# 3. 의존성 파일 복사 및 설치: requirements.txt를 먼저 복사하여 라이브러리를 설치합니다.
#    이렇게 하면 코드가 변경될 때마다 라이브러리를 다시 설치하지 않아 효율적입니다.
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 전체 복사: 현재 디렉토리의 모든 파일을 컨테이너의 /app 폴더로 복사합니다.
COPY . .

# 5. 서버 실행: Cloud Run이 컨테이너를 시작할 때 실행할 명령어입니다.
#    - 0.0.0.0: 컨테이너 외부에서 접근 가능하도록 설정합니다.
#    - 8080: Cloud Run이 기본적으로 사용하는 포트입니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
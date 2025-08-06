# frontend/Dockerfile

# 1. Node.js 베이스 이미지 선택
FROM node:20-alpine


# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. package.json 파일들 복사
COPY package*.json ./

# 4. 의존성 설치
RUN npm install

# 5. 소스코드 전체 복사
COPY . .

# 6. Vite 개발 서버 실행 (컨테이너 외부에서 접근 가능하도록 --host 추가)
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
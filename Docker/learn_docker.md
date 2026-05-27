https://www.youtube.com/watch?v=Gh1Sgknc6Fg
# 1. Giải thích dockerfile này thử tự clone https://github.com/docker/welcome-to-docker và đọc hiểu bên dưới và tạo docker image nhé: 
FROM node:22-alpine

=>  kế thừa từ image node:22-alpine

WORKDIR /app
=> thiết lập thư mục làm việc trong container là /app

COPY package*.json ./
=> sao chép file package.json và package-lock.json vào thư mục làm việc của container

COPY ./src ./src
COPY ./public ./public

RUN npm install \
    && npm install -g serve@latest \
    && npm run build \
    && rm -fr node_modules

=> chạy để tại thư viện

EXPOSE 3000
=> mở cổng 3000 để có thể truy cập vào ứng dụng từ bên ngoài container

CMD [ "serve", "-s", "build" ]
=> chạy câu lệnh gì trên máy của chúng ta

### Tạo docker image bằng cách chạy lệnh sau trong terminal:
- docker build -t welcome-to-docker .
=> -t là cờ để chạy image với tên welcome-to-docker, . là đường dẫn đến dockerfile hiện tại

# 2.Tự build với dự án mình machine_learning
- chạy với ubuntu
- docker run -it  machine_learning bash 
=> chạy container từ image machine_learning và mở terminal bash trong container đó để có thể tương tác với nó.
- Nếu chạy cài thư viện thành công trên  terminal/cmd/powershell thì mình đặt nó vào trong Dockerfile để khi build image nó sẽ tự động cài đặt thư viện đó vào image luôn.

- update hệ thống: RUN apt-get update
- cài đặt thư viện: RUN apt-get install -y python3 
- chayj python3 ml.py: CMD ["python3", "ml.py"]
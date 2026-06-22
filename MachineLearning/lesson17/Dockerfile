# Vào trang docker hub để kế thừa một vài image có sẵn không cần viết lại từ đầu
# vào trang docker hub https://hub.docker.com
# Dùng ubuntu, hoặc bất kỳ hệ điều hành nào khác
FROM ubuntu:24.04

# chú thích: name có thể đặt tên bất kỳ
# build image: docker build -t name .  (. là tìm Docker file để build image)
# chạy container: docker run name 
# chạy container có thể tương tác với container đó: docker run -it name
# thoát khỏi container: ctrl + D
# ls: liệt kê thư mục

WORKDIR /gia_thinh 
RUN apt update
RUN apt install python3 python3-pandas python3-sklearn -y
RUN apt install vim -y
COPY classification.py . 
COPY diabetes.csv .

# chạy cài thư viện ở ubuntu -> apt update -> apt install python3
# chạy -y để xác nhận cài đặt (bước xác nhận khi cài thủ công)
# Một khi thay đổi ở docker file, thì chạy build image mới
# RUN chạy để cài đặt thư viện
# vim giúp đọc file

# WORKDIR khi chạy docker nó sẽ vào thư mục gia-thinh
# COPY file code và data vào container

CMD ["python3", "classification.py"]
# chạy sau khi run container

# push lên docker hub để người khác có thể sử dụng được (tương tự github, docker pull ...)

# # Đăng nhập
# docker login
# # Build image với định dạng: <username>/<tên_image>:<phiên_bản>
# docker build -t username_cua_ban/ten_image:v1 .
# # Đưa lên Docker Hub
# docker push username_cua_ban/ten_image:v1
# # Tải về từ Docker Hub
# docker pull username_cua_ban/ten_image:v1

# ví dụ:
# docker build -t lamgiathinh2005/classification:v1 .
# docker push lamgiathinh2005/classification:v1
# docker pull lamgiathinh2005/classification:v1
# docker run lamgiathinh2005/classification:v1

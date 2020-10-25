FROM alpine:3.7

RUN apk add python3=3.6.9-r1

COPY "hmwk_docker.py" "/home/hmwk_docker.py"

ENTRYPOINT [ "python3", "/home/hmwk_docker.py" ]

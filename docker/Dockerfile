FROM ubuntu:22.04
RUN apt-get update
RUN apt install python-is-python3 -y
RUN mkdir /app
COPY mycode.py /app/mycode.py

CMD ["/app/mycode.py > /tmp/out"]

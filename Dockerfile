FROM ubuntu
LABEL maintainer="Guilherme Andre <gwandre@gmail.com>"

RUN apt-get update -y
RUN apt-get upgrade -qy
RUN apt-get install -qy python3 python3-pip python3-flask

WORKDIR /opt/app

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "./app.py"]

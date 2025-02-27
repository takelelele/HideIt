FROM ubuntu

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /opt/app/

COPY . .

RUN pip3 install --break-system-packages -r requirements.txt

ENTRYPOINT ["python3","main.py"]
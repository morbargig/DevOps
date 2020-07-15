FROM ubuntu:16.04
COPY ./project /project
RUN apt update
RUN apt install -y python3-pip && pip3 install --upgrade pip
RUN apt install -y postgresql postgresql-server-dev-9.5
RUN apt-get install rsync
RUN apt-get -y install curl
WORKDIR /project
# RUN rm -rf static
RUN pip3 install -r requirements.txt
COPY ./project/static /static

# ENTRYPOINT python3 manage.py
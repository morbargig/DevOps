FROM python
WORKDIR /app
RUN python -m pip install --upgrade pip
COPY /app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh","-c","while true; do sleep 3600; done" ]





FROM alpine:3.9
COPY . /myApp
RUN apk add --update nodejs npm
RUN apk add  --update python2
RUN  apk add --update py-pip
WORKDIR /myApp/project/flask-app
RUN npm install 
RUN npm run build 
RUN pip install -r requirements.txt
RUN python /myApp/project/utils/generate_geojson.py
ENTRYPOINT python app.py
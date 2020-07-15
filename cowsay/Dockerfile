FROM alpine:3.9
COPY ./cowsay-jenkins /myApp
RUN apk add --update npm
WORKDIR /myApp/src
RUN npm install
ENTRYPOINT node index.js
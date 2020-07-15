FROM maven:3.6.3-ibmjava-8-alpine
COPY project /project
WORKDIR /project
RUN mvn verify
RUN npm install
ENTRYPOINT ["mvn", "stampo:serve"]
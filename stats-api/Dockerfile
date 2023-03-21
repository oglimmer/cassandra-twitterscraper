FROM node

COPY . /opt/app

WORKDIR /opt/app

RUN npm i

ARG user
ARG password
ARG host
ARG database

RUN echo "user=$user" > .env
RUN echo "password=$password" >> .env
RUN echo "host=$host" >> .env
RUN echo "database=$database" >> .env

EXPOSE 3000

CMD ["node", "app.js"]
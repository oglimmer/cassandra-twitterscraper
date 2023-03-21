FROM python

RUN pip install snscrape cassandra-driver && apt update && apt -y install netcat

COPY . /opt/app

WORKDIR /opt/app

ARG API_url
ARG API_secret
ARG instance_name

ARG user
ARG password
ARG servers
ARG keyspace
ARG table

RUN echo "{" > conf.json
RUN echo "\"API_url\": \"$API_url\"," >> conf.json
RUN echo "\"API_secret\": \"$API_secret\"," >> conf.json
RUN echo "\"instance_name\": \"$instance_name\"," >> conf.json

RUN echo "\"user\": \"$user\"," >> conf.json
RUN echo "\"password\": \"$password\"," >> conf.json
RUN echo "\"servers\": $servers," >> conf.json
RUN echo "\"keyspace\": \"$keyspace\"," >> conf.json
RUN echo "\"table\": \"$table\"" >> conf.json

RUN echo "}" >> conf.json

ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "main.py"]

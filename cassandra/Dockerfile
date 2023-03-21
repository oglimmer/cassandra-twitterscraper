FROM cassandra

RUN mkdir -p /opt/app

COPY setup.sql /opt/app/
COPY init-db.sh /opt/app/

WORKDIR /opt/app

CMD ["./init-db.sh"]



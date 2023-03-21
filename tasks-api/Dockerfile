FROM python

RUN pip install mysql-connector-python-rf python-dotenv flask && apt update && apt -y install netcat

COPY . /opt/app

WORKDIR /opt/app

EXPOSE 3000

ENTRYPOINT ["./entrypoint.sh"]
CMD ["python", "api.py"]

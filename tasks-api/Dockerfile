FROM python

RUN pip install mysql-connector-python-rf python-dotenv flask

COPY . /opt/app

WORKDIR /opt/app

EXPOSE 3000

CMD ["python", "api.py"]

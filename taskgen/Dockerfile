FROM python

RUN pip install mysql-connector-python-rf python-dotenv

COPY . /opt/app

WORKDIR /opt/app

CMD ["python", "gen.py"]

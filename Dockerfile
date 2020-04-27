FROM python:3

COPY catalog /catalog
COPY requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "catalog.main"]
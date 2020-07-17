FROM python:3.8

RUN mkdir -p /code/backend
WORKDIR /code/backend

COPY requirements.txt /code/backend
RUN pip install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app/ . 

EXPOSE 5000

CMD ["python", "app.py"]
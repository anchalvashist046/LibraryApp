FROM python:3.13-slim-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind=0.0.0.0:5000", "wsgi:app"]

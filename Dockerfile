FROM python:3.12

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "--bind=0.0.0.0:8000", "wsgi:app"]

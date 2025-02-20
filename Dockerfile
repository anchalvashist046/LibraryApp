FROM python:3.12

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["./venv/bin/gunicorn", "--bind=0.0.0.0:8000", "wsgi:app"]

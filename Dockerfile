FROM python:3.12.3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD [ "gunicorn", "--bind",  "0.0.0.0:8000", "khana_pina.wsgi:application", "--workers=3"]

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
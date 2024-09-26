FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./app/requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

EXPOSE 5000

CMD ["python", "run.py"]

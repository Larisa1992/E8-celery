FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD . /app
WORKDIR /app
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
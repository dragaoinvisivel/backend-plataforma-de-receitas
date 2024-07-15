FROM python:latest

RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 5050

CMD [ "python", "app.py" ]
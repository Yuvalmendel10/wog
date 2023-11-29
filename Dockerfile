FROM python:3.8-slim

WORKDIR /app

COPY . /app

COPY scores.txt /scores.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=main_score.py

CMD ["flask", "run", "--host=0.0.0.0"]

FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY app/ .

CMD ["sh", "-c", "python main.py --reload"]
FROM python:3.10-slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt .

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "mobile_api.wsgi:application", "--bind", "0:8000" ] 
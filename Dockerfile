FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:create_app()"]
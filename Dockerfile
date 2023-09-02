FROM python:3.9

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ /app

# CMD ["python", "manage.py" ,"flask", "run", "--host", "0.0.0.0"]
# CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
CMD ["python", "manage.py" ]

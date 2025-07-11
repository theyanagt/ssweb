FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    wget unzip xvfb libxi6 libgconf-2-4 libnss3 libxss1 libasound2 libatk1.0-0 libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask selenium webdriver-manager

COPY app.py /app.py

CMD ["python", "/app.py"]

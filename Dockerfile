FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    firefox-esr \
    wget \
    curl \
    xvfb \
    default-jdk \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/2.35.1/allure-2.35.1.tgz && \
    tar -zxvf allure-2.35.1.tgz -C /opt/ && \
    ln -s /opt/allure-2.35.1/bin/allure /usr/bin/allure && \
    rm allure-2.35.1.tgz

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install allure-pytest

RUN mkdir -p /app/allure-results

CMD ["sh", "-c", "Xvfb :99 -screen 0 1920x1080x24 & export DISPLAY=:99 && sleep 5 && python -m pytest -v -s --alluredir=allure-results"]
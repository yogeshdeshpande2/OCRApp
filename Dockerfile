FROM python:3.7-slim

RUN apt update
RUN apt-get install -y build-essential python3-dev

WORKDIR /usr/src

RUN mkdir -p /usr/src/OCRApp
RUN mkdir -p /usr/src/OCRApp/images
RUN mkdir -p /usr/src/OCRApp/text

COPY requirements.txt .
COPY logging.json .
COPY config.yml .
COPY main.py .
COPY utils.py .
COPY test.py .
COPY error.log .
COPY info.log .


COPY ./images/ /usr/src/images/

RUN apt update
RUN apt install -y tesseract-ocr
RUN apt install -y libtesseract-dev
RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

#RUN rm -rf ~/.cache/pip
RUN echo 'export ETL_FRAMEWORK_HOME=/usr/src/OCRApp' >> ~/.bashrc 


ENV QUART_ENV="Test"

# Expose port 80
EXPOSE 80

VOLUME /logs

CMD ["python -u /usr/src/main.py" && "python -u /usr/src/test.py" ]
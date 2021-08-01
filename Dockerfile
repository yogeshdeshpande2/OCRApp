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

RUN sudo apt update
RUN sudo apt install tesseract-ocr
RUN sudo apt install libtesseract-dev

RUN pip install --no-cache-dir cython
RUN pip install --disable-pip-version-check --no-cache-dir -r requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir hypercorn[uvloop]
RUN rm -rf ~/.cache/pip



ENV QUART_ENV="Test"

# Expose port 80
EXPOSE 80

VOLUME /logs

CMD ["python", "main.py"]
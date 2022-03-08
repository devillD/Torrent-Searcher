FROM ghcr.io/devilld/py-dev

WORKDIR /BOT

RUN chmod -R 777 /BOT

COPY requirements.txt .
RUN pip3 install --no-cache -r requirements.txt

COPY piratebay.py .
CMD ["python3", "piratebay.py"]

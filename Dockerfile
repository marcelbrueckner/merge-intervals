FROM python:3.9.5-slim-buster
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "merge.py"]

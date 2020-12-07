FROM python:3.8.6-slim
#FROM python:3.8.6-alpine3.12

WORKDIR /app
ADD . /app
## Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT [ "python3", "server.py" ]

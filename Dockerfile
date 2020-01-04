# Run (build image): docker build -t events .

# Run (create container): docker run -it --rm --name events events  # Container name / image name

FROM python:3

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
# Require Redis

# Run (build image): docker build -t events .

# Run (create container): docker run -it --rm --name events events  # Container name / image name

FROM python:3

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# CMD ['python', './source/start.py']  # Disabled to work with Docker Compose
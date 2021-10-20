# It's not necessaryt to build this image alone, once the
# composer will build it automatically, but if it's necessary
# for debug purposes 
# 
# Build a image named events `docker build -t events .`
#
# Create a container based on the events image `docker run -it --rm --name events events`, first the container name and them the image name

FROM python:3

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
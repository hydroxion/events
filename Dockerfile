# Run (build): docker build -t events .

# Run (container): docker run -it --rm --name events events # Container / image name

FROM python:3

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# CMD ['python', 'start.py'] # Depends of Redis locally
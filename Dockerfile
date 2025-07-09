#Base Image
#FROM python:3.12.3-alpine
FROM python:3.14.0b3-alpine3.22

# App
WORKDIR /app
COPY main.py ./

#Requirments.txt
#RUN pip3 install Flask==3.1.0
RUN pip3 install Flask==3.1.1

ENTRYPOINT ["python3", "main.py"]

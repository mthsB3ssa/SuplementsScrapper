FROM python:3.7.16-bullseye

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY . .

WORKDIR src
CMD [ "python", "main.py" ]
FROM python:latest

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt 
RUN python -m pip install --upgrade pip

COPY . . 


EXPOSE 5050

CMD ["python" , "app.py"]
FROM python:3.8

WORKDIR /src/app
COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["src/app.py"]
#CMD ["flask", "run", "--host", "0.0.0.0"]

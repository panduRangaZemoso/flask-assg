FROM python:3.8-alpine

WORKDIR /src/app
COPY . .

RUN pip install -r src/requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
#CMD ["flask", "run", "--host", "0.0.0.0"]

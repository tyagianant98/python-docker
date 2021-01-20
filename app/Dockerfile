FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r dependencies.txt
ENTRYPOINT [ "python" ]
EXPOSE 8080
CMD ["server.py"]